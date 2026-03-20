"""News and event service with API integration and mock fallback support."""

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
NEWS_API_URL = "https://newsdata.io/api/1/news"

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


def _mock_event_text() -> str:
    """Return a mock city-level event label when the live API is unavailable."""
    fallback_events = [
        "normal day",
        "festival",
        "political rally",
        "strike",
    ]
    return random.choice(fallback_events)


def fetch_events(city: str) -> str:
    """Fetch event-related news headlines for a city.

    Attempts to call the NewsData.io news endpoint first. If the API key is
    missing, the request fails, no results are returned, or the response is
    malformed, mock text is returned instead.

    Args:
        city: City name used to scope the news query.

    Returns:
        A single string containing the top five article headlines, or a mock
        event label when the API path is unavailable.
    """
    api_key = _get_env_value("NEWSDATA_API_KEY") or _get_env_value("NEWS_API_KEY")
    if not api_key or requests is None:
        return _mock_event_text()

    params = {
        "q": city,
        "apikey": api_key,
    }

    try:
        response = requests.get(NEWS_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # NewsData.io returns article data inside the `results` collection.
        articles = data.get("results", [])[:5]
        combined_entries = []

        for article in articles:
            title = (article.get("title") or "").strip()
            description = (article.get("description") or "").strip()

            if title and description:
                combined_entries.append(f"{title} {description}")
            elif title:
                combined_entries.append(title)
            elif description:
                combined_entries.append(description)

        if not combined_entries:
            return _mock_event_text()

        return " | ".join(combined_entries)
    except (KeyError, TypeError, ValueError, requests.RequestException):
        return _mock_event_text()
