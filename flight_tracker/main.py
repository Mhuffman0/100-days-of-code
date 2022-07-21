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

# users = dm.get_customers()["users"]

users = [
    {
        "firstName": "Michael",
        "lastName": "Huffman",
        "email": "mhuffman012@gmail.com",
        "id": 1,
    },
    {
        "firstName": "Mike",
        "lastName": "Huff",
        "email": "huffman.michael30@gmail.com",
        "id": 2,
    },
]

prices = [
    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 2000, "id": 9},
    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 2000, "id": 10},
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
    email_from_addr=os.environ["EMAIL_ADDRESS"],
    email_password=os.environ["EMAIL_PASSWORD"],
)

fs.search_for_iata_codes(dm)
fs.search_for_flights()

for flight in fs.desired_flights:
    if flight.actual_price < flight.lowest_price:
        for user in users:

            # nm.send_text_message(flight)
            nm.send_email(email_to=user["email"], flight=flight)


# dm.customer_sign_up()
