from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(
        self,
        twillio_account_id=None,
        twillio_auth_token=None,
        twillio_phone_number=None,
        my_phone_number=None,
    ):
        self.twillio_client = Client(twillio_account_id, twillio_auth_token)
        self.twillio_phone_number = twillio_phone_number
        self.my_phone_number = my_phone_number

    def send_text_message(self, flight: FlightData):
        message = self.twillio_client.messages.create(
            body=str(flight),
            from_=self.twillio_phone_number,
            to=self.my_phone_number,
        )
        print(message.status)
