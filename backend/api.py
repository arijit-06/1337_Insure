"""FastAPI surface for exposing processed zone disruption results."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

try:
    import main as pipeline_main
except ImportError:  # pragma: no cover - supports package-style imports
    from backend import main as pipeline_main


app = FastAPI()


class RiskRequest(BaseModel):
    """Request body for nearest-zone risk inference."""

    lat: float
    lng: float
    city: str


def _validate_city(city: str) -> str:
    """Validate that the requested city exists in the configured city set."""
    normalized_city = city.lower()
    if normalized_city not in pipeline_main.CITIES:
        raise HTTPException(status_code=404, detail=f"Unknown city: {city}")
    return normalized_city


def _get_city_zones(city: str) -> list:
    """Return stored zones for a city, with readiness checks."""
    normalized_city = _validate_city(city)

    if not pipeline_main.CITY_RESULTS:
        raise HTTPException(status_code=503, detail="data not ready")

    zones = pipeline_main.CITY_RESULTS.get(normalized_city)
    if zones is None:
        raise HTTPException(status_code=503, detail="data not ready")

    if not zones:
        raise HTTPException(status_code=404, detail=f"No zone data available for city: {city}")

    return zones


def _get_last_updated(city: str) -> str | None:
    """Return the latest refresh timestamp for a city, if available."""
    return pipeline_main.LAST_UPDATED.get(city)


def find_nearest_zone(lat: float, lng: float, zones: list) -> dict | None:
    """Find the nearest zone using squared Euclidean distance."""
    nearest_zone = None
    nearest_distance = None

    for zone in zones:
        zone_lat = float(zone.get("lat", 0.0))
        zone_lng = float(zone.get("lng", 0.0))
        distance = (zone_lat - lat) ** 2 + (zone_lng - lng) ** 2

        if nearest_distance is None or distance < nearest_distance:
            nearest_distance = distance
            nearest_zone = zone

    return nearest_zone


def _build_risk_response(city: str, zone: dict) -> dict:
    """Build the API response payload for a nearest-zone risk lookup."""
    result = zone.get("result", {})
    return {
        "city": city,
        "zone_id": zone.get("zone_id"),
        "lat": zone.get("lat"),
        "lng": zone.get("lng"),
        "timestamp": zone.get("timestamp"),
        "last_updated": _get_last_updated(city),
        "risk_level": result.get("risk_level"),
        "disruption_score": result.get("disruption_score"),
        "downtime": result.get("downtime"),
        "reason": result.get("reason"),
    }


@app.get("/cities")
def get_cities() -> list:
    """Return the configured Tamil Nadu cities."""
    return [
        {
            "city": city,
            "code": config["code"],
            "tier": config["tier"],
            "state": config["state"],
        }
        for city, config in pipeline_main.CITIES.items()
    ]


@app.get("/zones")
def get_zones(city: str) -> list:
    """Return the latest in-memory zone processing results for a city."""
    normalized_city = _validate_city(city)
    return _get_city_zones(normalized_city)


@app.get("/analytics")
def get_analytics(city: str) -> dict:
    """Return aggregate analytics for a single city."""
    normalized_city = _validate_city(city)
    if not pipeline_main.CITY_ANALYTICS:
        raise HTTPException(status_code=503, detail="data not ready")

    analytics = pipeline_main.CITY_ANALYTICS.get(normalized_city)
    if analytics is None:
        raise HTTPException(status_code=503, detail="data not ready")

    return analytics


@app.get("/zones/high-risk")
def get_high_risk_zones(city: str) -> list:
    """Return only high-risk zones for the requested city."""
    normalized_city = _validate_city(city)
    return [
        zone
        for zone in _get_city_zones(normalized_city)
        if zone.get("result", {}).get("risk_level") == "HIGH"
    ]


@app.get("/risk")
def get_risk(lat: float, lng: float, city: str) -> dict:
    """Return the nearest zone's stored risk result for query coordinates."""
    normalized_city = _validate_city(city)
    zones = _get_city_zones(normalized_city)
    nearest_zone = find_nearest_zone(lat, lng, zones)

    if nearest_zone is None:
        raise HTTPException(status_code=404, detail="No zone match found")

    return _build_risk_response(normalized_city, nearest_zone)


@app.post("/risk")
def post_risk(request: RiskRequest) -> dict:
    """Return the nearest zone's stored risk result for posted coordinates."""
    normalized_city = _validate_city(request.city)
    zones = _get_city_zones(normalized_city)
    nearest_zone = find_nearest_zone(request.lat, request.lng, zones)

    if nearest_zone is None:
        raise HTTPException(status_code=404, detail="No zone match found")

    return _build_risk_response(normalized_city, nearest_zone)
