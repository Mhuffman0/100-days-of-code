from data_manager import make_request, DataManager


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, fly_from: str,  kiwi_auth_token: str, desired_flights: list):
        self.fly_from = fly_from
        self.kiwi_auth_token = kiwi_auth_token
        self.desired_flights = desired_flights

    def search_for_iata_codes(self, datamanager: DataManager):
        kiwi_headers = {"apikey": self.kiwi_auth_token}
        for row in self.desired_flights:
            if not row["iataCode"]:
                row["iataCode"] = make_request(
                    request_type="get",
                    params={"term": row["city"]},
                    url="https://tequila-api.kiwi.com/locations/query",
                    headers=kiwi_headers,
                )["locations"][0]["code"]
                datamanager.update_iata_codes(
                    iata_code=row["iataCode"], row_id=row["id"]
                )

    # def search_for_flights(self):
    #     for row in self.desired_flights:
    #         params = {
    #             "fly_from": self.fly_from,
    #             "fly_to": row["iata_code"],
    #         }
    #     # for the flight prices from London (LON) to all the destinations in the Google Sheet.In this project, we're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time. We're also looking for round trips that return between 7 and 28 days in length.The currency of the price we get back should be in GBP.
    #     # https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
