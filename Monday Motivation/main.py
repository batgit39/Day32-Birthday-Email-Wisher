import random
import datetime as dt
import smtplib

my_email = "" # your email
recievers_email = "" # recievers email 
password = "" # your gmail app's password
    
def weekday():
    now = dt.datetime.now()
    return now.weekday()

def random_quote():
    with open("./quotes.txt","r") as file:
        all = file.readlines()
        chosen_quote = random.choice(all)
        return chosen_quote

def send_monday_motivation():
    if weekday() == 1: # monday starts from 0, tuesday is 1...
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                    from_addr = my_email,
                    to_addrs = recievers_email,
                    msg = f"Subject:Monday Motivation\n\n{random_quote()}"
                    )

send_monday_motivation()
