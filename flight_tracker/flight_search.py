class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, data: dict):
        self.city = data["city"]
        self.iata_code = data["iataCode"]
        self.lowest_price = data["lowestPrice"]
        self.id = data["id"]

    def search_for_iata_code(self):
        print(f"Searching for {self.city}")
        self.iata_code = "TESTING2"

    def return_sheetsy_formatted_data(self):
        return {
            "price": {
                "iataCode": self.iata_code,
            }
        }
