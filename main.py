# import smtplib
#
my_email = "Your Email"
password = "Your Password"

SMTP_GMAIL = "smtp.gmail.com"
#
# connection = smtplib.SMTP(host=SMTP_GMAIL)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="Detination Email", msg="Subject:Test \nHello world")
# connection.close()

# import datetime as dt
# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=_, month=_, day=_)
# print(date_of_birth)

# Sending Motivational Emails
import datetime as dt
from random import choice
import smtplib

with open("quotes.txt") as file:
    quotes = file.readlines()

# Monday - 0, Tuesday - 1, Wednesday - 2, Thursday - 3, Friday - 4, Saturday - 5, Sunday - 6

now = dt.datetime.now()
curr_day = now.weekday()
random_quote = choice(quotes)

with smtplib.SMTP(host=SMTP_GMAIL) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Motivational Quote\n{random_quote}")
