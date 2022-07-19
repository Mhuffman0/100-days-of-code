from data_manager import make_request, DataManager
from flight_data import FlightData
import datetime

MIN_TIME_IN_CITY = 7
MAX_TIME_IN_CITY = 28
DAYS_TO_LOOK_FORWARD = 180


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(
        self, fly_from: str, kiwi_auth_token: str, desired_flights: list[dict]
    ):
        def populate_desired_flights(desired_flights):
            return [FlightData(row) for row in desired_flights]

        self.fly_from = fly_from
        self.kiwi_auth_headers = {"apikey": kiwi_auth_token}
        self.desired_flights = populate_desired_flights(desired_flights)
        self.great_deals = []

    def search_for_iata_codes(self, datamanager: DataManager):
        for row in self.desired_flights:
            if not row.iata_code:
                row.iata_code = make_request(
                    request_type="get",
                    params={"term": row.city},
                    url="https://tequila-api.kiwi.com/locations/query",
                    headers=self.kiwi_auth_headers,
                )["locations"][0]["code"]
                datamanager.update_iata_codes(iata_code=row.iata_code, row_id=row.id)

    def search_for_flights(self):
        today = datetime.date.today()
        tomorrow = (today + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        max_look_forward_date = (
            today + datetime.timedelta(days=DAYS_TO_LOOK_FORWARD)
        ).strftime("%d/%m/%Y")
        for row in self.desired_flights:
            params = {
                "fly_from": self.fly_from,
                "fly_to": row.iata_code,
                "max_stopovers": 0,
                "date_from": tomorrow,
                "date_to": max_look_forward_date,
                "nights_in_dst_from": MIN_TIME_IN_CITY,
                "nights_in_dst_to": MAX_TIME_IN_CITY,
                "flight_type": "round",
                "curr": "USD",
                "sort": "price",
                "limit": 1,
            }

            flight_info = make_request(
                request_type="get",
                params=params,
                url="https://tequila-api.kiwi.com/v2/search",
                headers=self.kiwi_auth_headers,
            )["data"]

            if flight_info and (
                flight_info[0]["price"]
                < [
                    flight.lowest_price
                    for flight in self.desired_flights
                    if flight.city == flight_info[0]["cityTo"]
                ][0]
            ):
                self.great_deals.append(flight_info)
