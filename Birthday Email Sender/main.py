import datetime as dt
import random
import pandas
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "" # your email
password = "" # your gmail app's password

def random_letter(name):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt","r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
        return letter

def birthday_records():
    data = pandas.read_csv("birthdays.csv")
    return data.to_dict(orient = "records")

def send_mail(email, letter):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
                from_addr = my_email,
                to_addrs = email,
                msg = f"Subject:Happy Birthday!\n\n{letter}"
                )

def checker():
    birthday = birthday_records()
    for person in birthday:
        if person['month'] == month and person['day'] == day:
            # print(person['email'])
            send_mail(person['email'], random_letter(person['name']))

checker()    

