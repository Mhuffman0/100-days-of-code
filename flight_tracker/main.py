"""This file combines the DataManager,FlightSearch, FlightData, NotificationManager classes."""
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os
from dotenv import load_dotenv


load_dotenv()

dm = DataManager(
    sheety_auth_token=os.environ.get("SHEETY_AUTH_TOKEN"),
    sheety_url=os.environ.get("SHEETY_URL"),
)

prices = [
    # {"city": "BALI", "iataCode": "", "lowestPrice": 2000, "id": 2},
    # {"city": "Berlin", "iataCode": "BER", "lowestPrice": 2000, "id": 3},
    # {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 2000, "id": 4},
    # {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 2000, "id": 5},
    # {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 2000, "id": 6},
    # {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 2000, "id": 7},
    # {"city": "New York", "iataCode": "NYC", "lowestPrice": 2000, "id": 8},
    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 2000, "id": 9},
    # {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 2000, "id": 10},
]

fs = FlightSearch(
    fly_from=os.environ.get("MY_CITY"),
    desired_flights=prices,  # dm.get_flight_data()["prices"],
    kiwi_auth_token=os.environ.get("KIWI_AUTH_TOKEN"),
)
nm = NotificationManager(
    twillio_account_id=os.environ["TWILLIO_ACCOUNT_SID"],
    twillio_auth_token=os.environ["TWILLIO_AUTH_TOKEN"],
    twillio_phone_number=os.environ["TWILLIO_PHONE_NUMBER"],
    my_phone_number=os.environ["MY_PHONE_NUMBER"],
)
#
fs.search_for_iata_codes(dm)
fs.search_for_flights()

for flight in fs.desired_flights:
    if flight.actual_price < flight.lowest_price:
        # print(flight)
        nm.send_text_message(flight)
# dm.customer_sign_up()
