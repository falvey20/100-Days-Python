import random
import pandas
import smtplib
from datetime import datetime as dt

MY_EMAIL = "walshs98@yahoo.com"
MY_PASSWORD = "vvpooeyzybdsdqfs"

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

today = dt.now()
today_tuple = (today.month, today.day)

bday_data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bday_data.iterrows()}

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    random_letter = random.choice(letters)
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter:
        contents = letter.read()
        letter_with_name = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=bday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter_with_name}"
                            )

