from twilio.rest import Client
from flight_data import FlightData
import smtplib


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(
        self,
        twillio_account_id=None,
        twillio_auth_token=None,
        twillio_phone_number=None,
        my_phone_number=None,
        email_from_addr=None,
        email_password=None,
    ):
        self.twillio_client = Client(twillio_account_id, twillio_auth_token)
        self.twillio_phone_number = twillio_phone_number
        self.my_phone_number = my_phone_number
        self.email_from_addr = email_from_addr
        self.email_password = email_password

    def send_text_message(self, flight: FlightData):
        message = self.twillio_client.messages.create(
            body=str(flight),
            from_=self.twillio_phone_number,
            to=self.my_phone_number,
        )
        print(message.status)

    def send_email(self, flight: FlightData, email_to: str):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email_from_addr, password=self.email_password)
            connection.sendmail(
                from_addr=self.email_from_addr,
                to_addrs=email_to,
                msg=f"Subject:Flight Alert\n\n{flight}",
            )
