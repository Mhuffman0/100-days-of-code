from dataclasses import dataclass


@dataclass
class FlightData:
    """This class is responsible for structuring the flight data."""

    destination_city: str
    iata_code: str
    lowest_price: int
    id: int
    actual_price: int = None
    link: str = None
    departure_date: str = None
    trip_length: int = None

    def __str__(self):
        return (f"""Great deal on flight to {self.destination_city} for ${str(self.actual_price)}.
Flight leaves on {self.departure_date} for and returns {self.trip_length} days later.
Click here to purchase:\n{self.link}""")

