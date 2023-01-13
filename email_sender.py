import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                        msg="Subject:Hello Testing Email\n\nThis is the body of my email and this is just a testing haii.")
