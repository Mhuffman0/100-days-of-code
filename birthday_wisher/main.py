from app_password import EMAIL_PASSWORD
import smtplib
import datetime
import random

EMAIL_ADDRESS = "huffman.michael30@gmail.com"
now = datetime.datetime.now()

if now.weekday() == 1:
    with open("quotes.txt") as quotes:
        quote = random.choice(quotes.readlines())

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs="mhuffman012@gmail.com",
            msg=f"Subject:Motivational Mondays\n\n{quote}",
        )
