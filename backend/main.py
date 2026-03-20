"""Main polling loop for zone-level disruption processing."""

from __future__ import annotations

import time
from datetime import datetime, timezone

try:
    from config.cities import CITIES
    from services.analytics import compute_city_analytics
    from services.news import fetch_events
    from services.processor import process_zone
    from utils.grid import generate_zones
except ImportError:  # pragma: no cover - supports package-style imports
    from backend.config.cities import CITIES
    from backend.services.analytics import compute_city_analytics
    from backend.services.news import fetch_events
    from backend.services.processor import process_zone
    from backend.utils.grid import generate_zones


CITY_RESULTS = {}
CITY_ANALYTICS = {}
LAST_UPDATED = {}


def _current_utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def refresh_city_results() -> tuple[dict, dict, dict]:
    """Process all configured Tamil Nadu cities sequentially.

    Returns:
        A tuple containing city-level zone results, city analytics, and
        per-city last updated timestamps.
    """
    all_city_results = {}
    all_city_analytics = {}
    all_last_updated = {}

    for city, city_config in CITIES.items():
        print(f"Processing {city}")
        zones = generate_zones(city_config, zone_prefix=city_config["code"])
        city_results = []

        try:
            events = fetch_events(city)
        except Exception:
            events = "normal day"

        for zone in zones:
            processed = process_zone(zone, city, events)
            city_results.append(processed)

        all_city_results[city] = city_results
        all_city_analytics[city] = compute_city_analytics(city, city_results)
        all_last_updated[city] = _current_utc_timestamp()
        print(f"{city} processed")

    return all_city_results, all_city_analytics, all_last_updated


def run_pipeline() -> None:
    """Continuously refresh in-memory results for all configured cities."""
    global CITY_RESULTS, CITY_ANALYTICS, LAST_UPDATED

    while True:
        print("Starting full refresh cycle...")
        CITY_RESULTS, CITY_ANALYTICS, LAST_UPDATED = refresh_city_results()
        print("Cycle complete. Sleeping for 1 hour...")
        time.sleep(3600)


if __name__ == "__main__":
    run_pipeline()
