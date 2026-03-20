"""Simple script for previewing generated Chennai zones."""

from utils.grid import CHENNAI_BOUNDS, generate_zones


def main() -> None:
    """Generate and print a sample of Chennai zones."""
    zones = generate_zones(CHENNAI_BOUNDS, step=0.08)

    print(f"Total zones: {len(zones)}")
    print()
    print("Sample zones:")

    for zone in zones[:5]:
        print(zone)

    if len(zones) > 5:
        print("...")

    for zone in zones[-5:]:
        print(zone)


if __name__ == "__main__":
    main()
