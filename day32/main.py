##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import random
import smtplib

EMAIL = "ama018807@gmail.com"
PASSWORD = "mewj jcda zzkg ehma"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
today = (now.month, now.day)
template = random.randint(1,3)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]["name"]
    birthday_email = birthday_dict[today]["email"]
    with open(f"letter_templates/letter_{template}.txt") as letter:
        content = letter.read()
        content_after = content.replace("[NAME]", birthday_person)
        print(content_after)

    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=birthday_email, msg=f"Subject: HAPPY BIRTHDAY!!\n\n{content_after}")


