from app_password import EMAIL_PASSWORD
import smtplib

EMAIL_ADDRESS = "huffman.michael30@gmail.com"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=EMAIL_ADDRESS,
        to_addrs="mhuffman012@gmail.com",
        msg="Subject:hello\n\nThis is the body of the email.",
    )

