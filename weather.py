import requests

def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_5_day_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def display_current_weather(data):
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']

    print(f"\nTemperature: {temperature}K")
    print(f"Weather: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Sunrise Time: {sunrise}")
    print(f"Sunset Time: {sunset}")

def display_5_day_forecast(data):
    for entry in data['list']:
        date = entry['dt_txt']
        temperature = entry['main']['temp']
        description = entry['weather'][0]['description']
        humidity = entry['main']['humidity']
        wind_speed = entry['wind']['speed']
        print(f"Date: {date}\n, Temperature: {temperature}K\n, Weather: {description}\n, Humidity: {humidity}%\n, Wind Speed: {wind_speed} m/s\n")

def main():
    api_key = '6c48ba85b939326060ff63112a8243c1'
    city = input("Enter city name: ")

    current_weather_data = fetch_weather_data(api_key, city)
    print("\nCurrent Weather Forecast:")
    display_current_weather(current_weather_data)

    forecast_data = fetch_5_day_forecast(api_key, city)
    print("\n5-Day Weather Forecast:\n")
    display_5_day_forecast(forecast_data)

if __name__ == "__main__":
    main()