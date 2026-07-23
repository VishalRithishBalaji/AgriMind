from pprint import pprint

from app.orchestrator.dynamic_orchestrator import dynamic_orchestrator


def main():

    result = dynamic_orchestrator.run(

        crop="Rice",

        location="Coimbatore",

        user_query="Should I irrigate my crop today?"

    )

    print()

    print("=" * 70)

    print("FINAL OUTPUT")

    print("=" * 70)

    pprint(result)


if __name__ == "__main__":

    main()