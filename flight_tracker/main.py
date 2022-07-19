"""This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements."""
from data_manager import DataManager
from flight_search import FlightSearch
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()

dm = DataManager(
    sheety_auth_token=os.environ.get("SHEETY_AUTH_TOKEN"),
    sheety_url=os.environ.get("SHEETY_URL"),
)

fs = FlightSearch(
    fly_from=os.environ.get("MY_CITY"),
    desired_flights=dm.get_flight_data()["prices"],
    kiwi_auth_token=os.environ.get("KIWI_AUTH_TOKEN"),
)
fs.search_for_iata_codes(dm)
fs.search_for_flights()

if fs.great_deals:
    for great_deal in fs.great_deals:
        client = Client(
            os.environ["TWILLIO_ACCOUNT_SID"], os.environ["TWILLIO_AUTH_TOKEN"]
        )
        message = client.messages.create(
            body=(
                f"Great deal on flight to {great_deal[0]['cityTo']} for ${great_deal[0]['price']}.\n"
                f"Click here to purchase:\n{great_deal[0]['deep_link']}"
            ),
            from_=os.environ["TWILLIO_PHONE_NUMBER"],
            to=os.environ["MY_PHONE_NUMBER"],
        )
        print(message.status)
