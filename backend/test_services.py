"""Simple test script for environmental and contextual services."""

from services.news import fetch_events
from services.traffic import fetch_traffic
from services.weather import fetch_weather


def main() -> None:
    """Fetch and print service data for a Chennai sample location."""
    lat = 13.08
    lon = 80.27
    city = "Chennai"

    weather = fetch_weather(lat, lon)
    traffic = fetch_traffic(lat, lon)
    events = fetch_events(city)

    print(f"Weather: {weather}")
    print(f"Traffic: {traffic}")
    print(f"Events: {events}")


if __name__ == "__main__":
    main()
