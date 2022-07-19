class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, destination):
        self.city = destination["city"]
        self.iata_code = destination["iataCode"]
        self.lowest_price = destination["lowestPrice"]
        self.id = destination["id"]
