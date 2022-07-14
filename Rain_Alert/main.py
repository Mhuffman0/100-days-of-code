import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

params = {
    "lat": os.environ["LATITUDE"],
    "lon": os.environ["LONGITUDE"],
    "appid": os.environ["OWM_API_KEY"],
    "exclude": ["current", "minutely", "daily", "alerts"],
}

response = requests.get(
    "https://api.openweathermap.org/data/3.0/onecall", params=params
)

response.raise_for_status()
forecast_for_next_twelve_hours = response.json()["hourly"][:12]

will_rain = [
    hour for hour in forecast_for_next_twelve_hours if hour["weather"][0]["id"] < 700
]
if will_rain:
    client = Client(os.environ["TWILLIO_ACCOUNT_SID"], os.environ["TWILLIO_AUTH_TOKEN"])
    message = client.messages.create(
        body="Bring an umbrella!",
        from_=os.environ["TWILLIO_PHONE_NUMBER"],
        to=os.environ["MY_PHONE_NUMBER"],
    )
    print(message.status)
