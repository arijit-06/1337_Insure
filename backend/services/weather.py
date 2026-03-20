"""Weather service with Tomorrow.io integration and mock fallback support."""

from __future__ import annotations

import os
import random
from datetime import datetime, timezone
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
WEATHER_API_URL = "https://api.tomorrow.io/v4/weather/realtime"

load_dotenv(ENV_PATH)


def _get_env_value(name: str) -> str | None:
    """Read configuration from environment variables or the local `.env` file."""
    value = os.getenv(name)
    if value:
        return value

    if not ENV_PATH.exists():
        return None

    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if "=" not in line:
            continue

        key, raw_value = line.split("=", 1)
        if key.strip() == name:
            cleaned_value = raw_value.strip()
            return cleaned_value or None

    return None


def _mock_weather() -> dict:
    """Return mock weather data when the live API is unavailable."""
    return {
        "rain": round(random.uniform(0, 100), 2),
        "temp": round(random.uniform(25, 40), 2),
        "observed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }


def _normalize_utc_timestamp(timestamp: str) -> str:
    """Normalize provider timestamps to a standard UTC ISO format."""
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).isoformat()


def fetch_weather(lat: float, lon: float) -> dict:
    """Fetch weather data for a geographic coordinate.

    Attempts to call the Tomorrow.io realtime weather API first. If the API
    key is missing, the request fails, or the response is malformed, mock data
    is returned instead.

    Args:
        lat: Latitude of the target location.
        lon: Longitude of the target location.

    Returns:
        A dictionary containing rainfall intensity in millimeters per hour,
        temperature in Celsius, and the source observation timestamp in UTC.
    """
    api_key = _get_env_value("TOMORROW_API_KEY")
    if not api_key or requests is None:
        return _mock_weather()

    params = {
        "location": f"{lat},{lon}",
        "apikey": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        values = data["data"]["values"]

        # Tomorrow.io exposes rain intensity as millimeters per hour.
        rain = float(values.get("rainIntensity", 0) or 0)
        temp = float(values["temperature"])
        return {
            "rain": round(rain, 2),
            "temp": round(temp, 2),
            "observed_at": _normalize_utc_timestamp(data["data"]["time"]),
        }
    except (KeyError, TypeError, ValueError, requests.RequestException):
        return _mock_weather()
