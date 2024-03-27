import requests

def get_weather_forecast(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={city['lat']}&lon={city['lon']}&exclude=current,minutely,hourly,alerts&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


city = {"lat": 51.5074, "lon": -0.1278}  # London's latitude and longitude
api_key = "e77e3b992349aab8f8c5ed9b3a429d42"

weather_forecast = get_weather_forecast(city, api_key)
print(weather_forecast)




