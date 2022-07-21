from dataclasses import dataclass
import datetime


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
    trip_length: int = 0

    def get_return_date(self) -> datetime:
        split_departure_date = self.departure_date.split("-")
        year = int(split_departure_date[0])
        month = int(split_departure_date[1])
        day = int(split_departure_date[2])
        departure_date = datetime.datetime(year=year, month=month, day=day)
        return (departure_date + datetime.timedelta(days=self.trip_length)).strftime(
            "%Y-%m-%d"
        )

    def __str__(self):
        return (
            f"Great deal on flight to {self.destination_city} for ${str(self.actual_price)}.\n"
            f"Flight leaves on {self.departure_date} for and returns on {self.get_return_date()}.\n\n"
            f"Click here to purchase:\n{self.link}"
        )
