
from pandas import *
import smtplib
from datetime import *
import random
import os

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

data=read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

now=datetime.now()
today_month=now.month
today_day=now.day

if (today_month,today_day) in birthdays_dict:
    file_path=f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path)as f:
        letter=f.read()
        new_letter=letter.replace("[NAME]", birthdays_dict[(today_month,today_day)]["name"])

    with  smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[(today_month,today_day)]["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")



