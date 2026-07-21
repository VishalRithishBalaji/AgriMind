from pprint import pprint

from app.memory.memory_manager import memory_manager


def main():

    results = memory_manager.retrieve(

        crop="Rice",

        weather="Hot and Dry",

        soil="Medium Nitrogen",

        market="Increasing",

        top_k=3

    )

    pprint(results)


if __name__ == "__main__":

    main()