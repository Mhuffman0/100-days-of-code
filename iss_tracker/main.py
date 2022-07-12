import requests
import smtplib
import time
from app_password import EMAIL_PASSWORD

LATITUDE = 41.990200
LONGITUDE = -70.975400
SENDER_EMAIL_ADDRESS = "huffman.michael30@gmail.com"
MY_EMAIL_ADDRESS = "mhuffman012@gmail.com"
DEGREES_OF_ERROR = 5


def get_response(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def sunrise_sunset_hour(response, value):
    hour = int(response["results"][value].split("T")[1].split(":")[0])
    if hour == 0:
        return 24
    else:
        return hour


def within_tolerance(current_value, desired_value):
    return abs(current_value - desired_value) < DEGREES_OF_ERROR


def is_night():
    sunrise_sunset_response = get_response(
        f"https://api.sunrise-sunset.org/json",
        {"lat": LATITUDE, "lng": LONGITUDE, "formatted": 0},
    )
    sunrise = sunrise_sunset_hour(sunrise_sunset_response, "sunrise")
    sunset = sunrise_sunset_hour(sunrise_sunset_response, "sunset")
    current_hour = time.gmtime().tm_hour
    return current_hour > sunset or current_hour < sunrise


def check_for_iss():
    if is_night():
        iss_response = get_response("http://api.open-notify.org/iss-now")
        iss_latitude = float(iss_response["iss_position"]["latitude"])
        iss_longitude = float(iss_response["iss_position"]["longitude"])
        if within_tolerance(LONGITUDE, iss_longitude) and within_tolerance(
            LATITUDE, iss_latitude
        ):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.login(user=SENDER_EMAIL_ADDRESS, password=EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=SENDER_EMAIL_ADDRESS,
                    to_addrs=MY_EMAIL_ADDRESS,
                    msg=f"Look up!",
                )


# while True:
check_for_iss()
# time.sleep(60)
print("hi")
