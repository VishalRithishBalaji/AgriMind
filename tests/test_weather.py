from pprint import pprint

from app.services.weather_service import weather_service


def main():

    weather = weather_service.get_current_weather()

    pprint(weather)


if __name__ == "__main__":

    main()