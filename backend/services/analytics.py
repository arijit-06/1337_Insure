"""Analytics helpers for city-level disruption summaries."""

from __future__ import annotations

from datetime import datetime, timezone


def compute_city_analytics(city: str, zone_results: list) -> dict:
    """Compute aggregate disruption analytics for a city's zone results.

    Args:
        city: City name for the analytics snapshot.
        zone_results: List of processed zone result dictionaries.

    Returns:
        A city-level analytics dictionary with averages and risk counts.
    """
    total_zones = len(zone_results)
    timestamp = datetime.now(timezone.utc).isoformat()

    if total_zones == 0:
        return {
            "city": city,
            "timestamp": timestamp,
            "avg_disruption": 0.0,
            "avg_downtime": 0.0,
            "high_risk_zones": 0,
            "medium_risk_zones": 0,
            "low_risk_zones": 0,
            "total_zones": 0,
        }

    disruption_total = 0.0
    downtime_total = 0.0
    high_risk_zones = 0
    medium_risk_zones = 0
    low_risk_zones = 0

    for zone in zone_results:
        result = zone.get("result", {})
        disruption_total += float(result.get("disruption_score", 0.0))
        downtime_total += float(result.get("downtime", 0.0))

        risk_level = result.get("risk_level")
        if risk_level == "HIGH":
            high_risk_zones += 1
        elif risk_level == "MEDIUM":
            medium_risk_zones += 1
        elif risk_level == "LOW":
            low_risk_zones += 1

    return {
        "city": city,
        "timestamp": timestamp,
        "avg_disruption": round(disruption_total / total_zones, 4),
        "avg_downtime": round(downtime_total / total_zones, 4),
        "high_risk_zones": high_risk_zones,
        "medium_risk_zones": medium_risk_zones,
        "low_risk_zones": low_risk_zones,
        "total_zones": total_zones,
    }
