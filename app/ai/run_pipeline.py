from pprint import pprint

from app.ai.pipeline import pipeline


def main():

    result = pipeline.execute(
        crop="rice"
    )

    print("\nFINAL PIPELINE OUTPUT\n")

    pprint(result)


if __name__ == "__main__":
    main()