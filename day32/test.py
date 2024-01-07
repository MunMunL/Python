##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import random

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
today = (now.month, now.day)
template = random.randint(1,3)

data = pandas.read_csv("birthdays.csv")
print(data)
for (index, data_row) in data.iterrows():
    print(data_row["month"])
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

if today in birthday_dict:
    birthday_person = birthday_dict[today]["name"]
    birthday_email = birthday_dict[today]["email"]
    with open(f"letter_templates/letter_{template}.txt") as letter:
        content = letter.read()
        content_after = content.replace("[NAME]", birthday_person)
        print(content_after)