from pprint import pprint

from app.tools.soil_tool import soil_tool


def main():

    soil = soil_tool.get_soil()

    assessment = soil_tool.assess_soil(soil)

    print("\n=== Soil Data ===")
    pprint(soil)

    print("\n=== Soil Assessment ===")
    pprint(assessment)


if __name__ == "__main__":
    main()