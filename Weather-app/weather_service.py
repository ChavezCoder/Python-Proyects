import os
import requests
from dotenv import load_dotenv

# Load enviroments variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name: str) -> dict:
    """
    Fetches a current weather data for a given city name.
    
    Returns a dictionary with formatted weather details on a error message.
    """

    if not API_KEY:
        return {"error": "API key not found in .env file" }

    if not city_name.strip():
        return {"error": "Please enter a valid city name."}

    # Query Parameters

    params = {
        "q":city_name,
        "appid": API_KEY,
        "units": "metric", # If you want to use Fahrenheit, use "imperal"
        "lang": "en"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temp": round(data["main"]["feels_like"]),
                "feels_like": data["main"]["humidity"],
                "description": data["weatgher"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"]
            }
        elif response.status_code == 404:
            return {"error": f"City '{city_name}' not found."}
        elif response.status_code == 401:
            return {"error":"Invalid API key or key is not active."}
        else:
            return {"error": f"Server Error: ({response.status_code}). Try again later."}
    except requests.exceptions.Timeout:
        return {"error": "Request time out. Check your internet connection."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error {str(e)}."} 

    # -- Terminal Test Run ---

if __name__ == "__main__":
    test_city = input("Enter a city name: ")
    weather = get_weather(test_city)
    print("\n--- Weather Result ---")
    if "error" in weather:
        print(f"❌ Error: {weather['error']}")
    else:
        print(f"📍 Location: {weather["city"]}, {weather['country']}.")
        print(f"🌡️ Temperature: {weather["temp"]}°C (Feels lie {weather['feels_like']}°C.)")
        print(f"☁️ Condition: {weather['description']}.")
        print(f"💧 Humidity: {weather['humidity']}%.")
        print(f"💨 Wind Speed: {weather['wind_speed']}%.")

