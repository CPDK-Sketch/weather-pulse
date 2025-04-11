import requests
import sys
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {
        'key': API_KEY,
        'q': city
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Wind: {data['current']['wind_kph']} kph")
        print(f"Humidity: {data['current']['humidity']}%")
    else:
        print("Error:", data.get("error", {}).get("message", "Failed to get data."))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <city>")
    else:
        get_weather(sys.argv[1])
