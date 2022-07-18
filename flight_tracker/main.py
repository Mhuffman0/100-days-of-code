"""This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements."""
from data_manager import DataManager
from flight_search import FlightSearch
import os
from dotenv import load_dotenv


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
