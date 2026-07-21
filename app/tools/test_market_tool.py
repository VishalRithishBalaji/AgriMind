from pprint import pprint

from app.tools.market_tool import market_tool


def main():

    pprint(

        market_tool.execute(

            crop="rice"

        )

    )


if __name__ == "__main__":

    main()