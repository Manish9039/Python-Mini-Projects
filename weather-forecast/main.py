import requests
import os
from datetime import datetime

def get_weather_data(location, user_api):
    try:
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data["cod"] == "404":
            print("City not found. Please enter a valid city name.")
            return None

        return api_data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def display_weather_data(api_data):
    if api_data:
        try:
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            humidity = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            print("-------------------------------------------------------------")
            print("Weather Stats for - {}  || {}".format(api_data['name'].upper(), date_time))
            print("-------------------------------------------------------------")
            print("Current temperature is: {:.2f} deg C".format(temp_city))
            print("Current weather desc  :", weather_desc)
            print("Current Humidity      :", humidity, '%')
            print("Current wind speed    :", wind_spd, 'kmph')
        except KeyError as e:
            print("Error processing data:", e)

def main():
    user_api = os.environ.get('current_weather_data')
    if not user_api:
        print("API key not found. Please set 'current_weather_data' environment variable.")
        return

    location = input("Enter the city name: ").strip()
    if not location:
        print("Please enter a city name.")
        return

    api_data = get_weather_data(location, user_api)
    display_weather_data(api_data)


if __name__ == "__main__":
    main()
