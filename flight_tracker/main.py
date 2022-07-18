# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

dm = DataManager(
    sheety_auth_token=os.environ.get("SHEETY_AUTH_TOKEN"),
    sheety_url=os.environ.get("SHEETY_URL"),
)
# sheety_data = {
#     "prices": {
#         "date": now.strftime("%d/%m/%Y"),
#         "time": now.strftime("%X"),
#         "exercise": workout["name"].title(),
#         "duration": workout["duration_min"],
#         "calories": workout["nf_calories"],
#     }
# }
# dm.get_flight_data()
temp_sheety = {
    "prices": [
        {"city": "Paris", "iataCode": "", "lowestPrice": 54, "id": 2},
        {"city": "Berlin", "iataCode": "a", "lowestPrice": 42, "id": 3},
        {"city": "Tokyo", "iataCode": "b", "lowestPrice": 485, "id": 4},
        {"city": "Sydney", "iataCode": "c", "lowestPrice": 551, "id": 5},
        {"city": "Istanbul", "iataCode": "d", "lowestPrice": 95, "id": 6},
        {"city": "Kuala Lumpur", "iataCode": "e", "lowestPrice": 414, "id": 7},
        {"city": "New York", "iataCode": "f", "lowestPrice": 240, "id": 8},
        {"city": "San Francisco", "iataCode": "g", "lowestPrice": 260, "id": 9},
        {"city": "Cape Town", "iataCode": "h", "lowestPrice": 378, "id": 10},
    ]
}

for row in temp_sheety["prices"]:
    fs = FlightSearch(row)
    if not fs.iata_code:
        fs.search_for_iata_code()
        dm.update_iata_codes(
            url=f"{dm.sheety_url}/{fs.id}", data=fs.return_sheetsy_formatted_data()
        )
