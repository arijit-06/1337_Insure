"""Utilities for generating deterministic geographic grid zones."""

from __future__ import annotations


CHENNAI_BOUNDS = {
    "lat_min": 12.90,
    "lat_max": 13.20,
    "lng_min": 80.10,
    "lng_max": 80.35,
}


def validate_bounds(bounds: dict) -> None:
    """Validate that geographic bounds contain the required numeric values."""
    required_keys = ("lat_min", "lat_max", "lng_min", "lng_max")

    for key in required_keys:
        if key not in bounds:
            raise ValueError(f"Missing required bounds key: {key}")

        if not isinstance(bounds[key], (int, float)):
            raise ValueError(f"Bounds value for '{key}' must be numeric")

    if bounds["lat_min"] >= bounds["lat_max"]:
        raise ValueError("lat_min must be less than lat_max")

    if bounds["lng_min"] >= bounds["lng_max"]:
        raise ValueError("lng_min must be less than lng_max")


def generate_zones(bounds: dict, step: float = 0.08, zone_prefix: str = "chn_") -> list:
    """Generate evenly spaced geographic zones for the provided bounds.

    Args:
        bounds: Dictionary containing `lat_min`, `lat_max`, `lng_min`, and
            `lng_max` values.
        step: Distance between adjacent grid points.
        zone_prefix: Prefix used to build deterministic zone identifiers.

    Returns:
        A list of dictionaries containing zone identifiers and coordinates.

    Raises:
        ValueError: If bounds are invalid or the step size is not positive.
    """
    validate_bounds(bounds)

    if step <= 0:
        raise ValueError("step must be greater than 0")

    zones = []
    zone_index = 0

    lat = bounds["lat_min"]
    while lat < bounds["lat_max"]:
        lng = bounds["lng_min"]

        # Iterate longitude for each latitude row to build a stable grid.
        while lng < bounds["lng_max"]:
            zones.append(
                {
                    "id": f"{zone_prefix}{zone_index}",
                    "lat": round(lat, 4),
                    "lng": round(lng, 4),
                }
            )
            zone_index += 1
            lng += step

        lat += step

    return zones
