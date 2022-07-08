from app_password import EMAIL_PASSWORD
import smtplib
import datetime
import random
import csv
import os

EMAIL_ADDRESS = "huffman.michael30@gmail.com"

now = datetime.datetime.now()

# Returns a list of friends with a birthday today
with open("birthdays.csv") as birthday_file:
    todays_birthdays = [
        row
        for row in csv.DictReader(birthday_file)
        if int(row["month"]) == now.month and int(row["day"]) == now.day
    ]

if todays_birthdays:
    for birthday_boy in todays_birthdays:
        # Formats random template letter
        with open(
            f"letter_templates\{random.choice(os.listdir('letter_templates'))}"
        ) as file:
            formatted_letter = file.read().replace("[NAME]", birthday_boy["name"])
        # Sends the birthday email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs=birthday_boy["email"],
                msg=f"Subject:Happy Birthday!\n\n{formatted_letter}",
            )
