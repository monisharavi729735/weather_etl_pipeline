import requests
import datetime
from dotenv import load_dotenv
import os

def extract():
    load_dotenv()  # loads variables from .env into the environment
    API_KEY = os.getenv("API_KEY")
    CITY = os.getenv("CITY")
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(URL)
    data = response.json()
    return {
        "city": CITY,
        "timestamp": datetime.datetime.now(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["main"]
    }