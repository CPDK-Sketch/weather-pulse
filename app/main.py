import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("WEATHER_API_KEY")

# Function to get weather info
def get_weather(city):
    print(f"\nGetting weather for: {city}")

    # API endpoint with parameters
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    # Make a request to the API
    response = requests.get(url)

    # If response is successful
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']

        print(f"📍 Location: {location}")
        print(f"🌡️ Temperature: {temp_c}°C")
        print(f"⛅ Condition: {condition}\n")
    else:
        print("❌ Error getting weather. Please check the city name or API key.\n")

# This runs when we run the file directly
if __name__ == "__main__":
    # Interactive input: ask the user for city
    city = input("Enter city name: ")  # Prompt the user to enter a city name

    # Call function
    get_weather(city)
