"""Simple test script for local LLM-based disruption analysis."""

from services.llm import get_llm_result


def main() -> None:
    """Call the local LLM analysis flow with sample data and print the result."""
    sample_data = {
        "rain": 80,
        "temp": 35,
        "traffic": "high",
        "events": "political rally in Chennai",
    }

    result = get_llm_result(sample_data)
    print(result)


if __name__ == "__main__":
    main()
