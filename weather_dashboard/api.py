import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return temp, desc
    else:
        print("Error:", data.get("message", "Unable to fetch weather"))
        return None, None
