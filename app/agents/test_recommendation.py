from pprint import pprint

from app.ai.orchestrator import orchestrator


def main():

    result = orchestrator.execute(
        crop="rice"
    )

    pprint(result["recommendation"])


if __name__ == "__main__":
    main()