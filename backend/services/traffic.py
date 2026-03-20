"""Traffic service with weighted mock behavior."""

from __future__ import annotations

import os
import random
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - handled through fallback behavior
    def load_dotenv(*args, **kwargs) -> bool:
        """Fallback no-op when python-dotenv is unavailable."""
        return False


ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(ENV_PATH)


def fetch_traffic(lat: float, lon: float) -> str:
    """Return a weighted mock traffic level for a geographic coordinate.

    Args:
        lat: Latitude of the target location.
        lon: Longitude of the target location.

    Returns:
        A simulated traffic severity label.
    """
    # Keep the traffic service mock-only for now, while still loading the
    # environment consistently with the other services for future expansion.
    _ = (lat, lon, os.getenv("OPENWEATHER_API_KEY"))

    traffic_levels = ["low", "medium", "high"]
    traffic_weights = [0.2, 0.5, 0.3]
    return random.choices(traffic_levels, weights=traffic_weights, k=1)[0]
