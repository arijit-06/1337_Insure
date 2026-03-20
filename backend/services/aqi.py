"""Air quality service with API integration and mock fallback support."""

from __future__ import annotations

import os
import random
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover - handled through fallback behavior
    requests = None

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - handled through fallback behavior
    def load_dotenv(*args, **kwargs) -> bool:
        """Fallback no-op when python-dotenv is unavailable."""
        return False


ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
AQI_API_URL = "https://api.openweathermap.org/data/2.5/air_pollution"
AQI_SCALE_MAP = {
    1: 50,
    2: 100,
    3: 150,
    4: 250,
    5: 400,
}

load_dotenv(ENV_PATH)


def _mock_aqi() -> int:
    """Return a mock AQI value when the live API is unavailable."""
    return random.randint(50, 300)


def fetch_aqi(lat: float, lon: float) -> int:
    """Fetch air quality data for a geographic coordinate.

    Attempts to call the OpenWeatherMap air pollution API first. If the API
    key is missing, the request fails, or the response is malformed, mock data
    is returned instead.

    Args:
        lat: Latitude of the target location.
        lon: Longitude of the target location.

    Returns:
        An approximate integer AQI value on a 0 to 500 style scale.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key or requests is None:
        return _mock_aqi()

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
    }

    try:
        response = requests.get(AQI_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        api_aqi = int(data["list"][0]["main"]["aqi"])
        return AQI_SCALE_MAP.get(api_aqi, _mock_aqi())
    except (KeyError, IndexError, TypeError, ValueError, requests.RequestException):
        return _mock_aqi()
