##################### Extra Hard Starting Project ######################
import os
import smtplib
import random
import pandas as pd
import datetime as dt


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
print("EMAIL:", os.environ.get("MY_EMAIL"))
print("PASSWORD EXISTS:", os.environ.get("MY_PASSWORD") is not None)
# 1. Update the birthdays.csv
bdays = pd.read_csv('birthdays.csv')
print(bdays.shape, "bdays shape check")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
print(f"day is {day}, month is {month} in now ")

recs = bdays.loc[(bdays['day'] == day) & (bdays['month'] == month)]
print(recs.shape, "shape of recs")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for index, rec in recs.iterrows():
    letter_files = os.listdir('letter_templates')
    print(letter_files, "letter files ")
    letter_f = random.choice(letter_files)
    with open (f"letter_templates/{letter_f}") as f:
        letter = f.read()

        updated_letter = letter.replace("[NAME]", rec["name"])
        updated_letter = updated_letter.replace("Angela","Nawal")
        print(updated_letter)
    #4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=rec['email'],msg = f"Subject: Happy Birthday!\n\n{updated_letter}")




