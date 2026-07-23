from pprint import pprint

from app.collectors.data_collector import data_collector


def main():

    result = data_collector.collect(
        crop="rice"
    )

    print()

    print("=" * 70)
    print("FINAL MULTI-SOURCE DATA OBJECT")
    print("=" * 70)

    pprint(result)


if __name__ == "__main__":
    main()