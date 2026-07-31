from pprint import pprint

from app.orchestrator.dynamic_orchestrator import dynamic_orchestrator


def main():

    print("=" * 80)
    print("AGRIMIND MODULE 5E TEST")
    print("=" * 80)

    result = dynamic_orchestrator.run(

        user_query="Should I irrigate my rice crop today?",

        crop="rice",

        latitude=11.0168,

        longitude=76.9558

    )

    print("\n")
    print("=" * 80)
    print("RAW RESULT")
    print("=" * 80)

    pprint(result)

    print("\n")
    print("=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)

    pprint(result["execution"]["recommendation"])


if __name__ == "__main__":
    main()