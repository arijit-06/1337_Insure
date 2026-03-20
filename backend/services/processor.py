"""Zone processing pipeline for environmental and disruption analysis."""

from __future__ import annotations

from datetime import datetime, timezone

try:
    from services.llm import FALLBACK_RESULT, get_llm_result
    from services.traffic import fetch_traffic
    from services.weather import fetch_weather
except ImportError:  # pragma: no cover - supports package-style imports
    from backend.services.llm import FALLBACK_RESULT, get_llm_result
    from backend.services.traffic import fetch_traffic
    from backend.services.weather import fetch_weather


def process_zone(zone: dict, city: str, events: str) -> dict:
    """Fetch live signals for a zone and compute disruption analysis.

    Args:
        zone: Zone dictionary containing `id`, `lat`, and `lng`.
        city: City name used for city-specific context and output metadata.
        events: Pre-fetched city-level event text reused across all zones.

    Returns:
        A dictionary containing the original zone metadata, fetched input data,
        and the structured LLM result.
    """
    lat = zone["lat"]
    lng = zone["lng"]

    try:
        weather = fetch_weather(lat, lng)
    except Exception:
        weather = {"rain": 0.0, "temp": 30.0}

    try:
        traffic = fetch_traffic(lat, lng)
    except Exception:
        traffic = "medium"

    data = {
        "rain": weather.get("rain", 0.0),
        "temp": weather.get("temp", 30.0),
        "traffic": traffic,
        "events": events,
    }

    try:
        result = get_llm_result(data)
    except Exception:
        result = FALLBACK_RESULT.copy()

    zone_timestamp = weather.get("observed_at") or datetime.now(timezone.utc).replace(
        microsecond=0
    ).isoformat()

    return {
        "zone_id": zone["id"],
        "city": city,
        "lat": lat,
        "lng": lng,
        "timestamp": zone_timestamp,
        "data": data,
        "result": result,
    }
