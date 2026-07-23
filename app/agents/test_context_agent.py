from pprint import pprint

from app.agents.context_agent import context_agent


def main():

    context = context_agent.build_context(

        crop="rice"

    )

    print()

    print("=" * 70)

    print("UNIFIED FARM CONTEXT")

    print("=" * 70)

    pprint(context)


if __name__ == "__main__":

    main()