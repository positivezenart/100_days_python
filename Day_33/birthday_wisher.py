import pandas as pd
import datetime as dt
import smtplib

df = pd.read_csv('Day_33/birthdays.csv')
df_list = df.to_dict(orient="records")

my_email ="maheshmj200@gmail.com"
password = "cofpwvteidavizto"

for ele in df_list:
    date_of_birth = dt.datetime(year=ele['year'],month=ele['month'],day=ele['day']).strftime("%Y-%m-%d")
    today =dt.datetime.today().strftime("%Y-%m-%d")
    if date_of_birth ==today:
        with open("Day_33\letter_templates\letter_3.txt","r") as file:
             data =file.readlines()
        data[0]= data[0].replace("[NAME]",ele['name'])
        birthday_wish =" ".join(map(str,data))
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # To keep connection is sure, It will encrypt the email address
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=ele['email'],
                                msg=f"Subject:Happy Birthday \n\n {birthday_wish}")
        print(f"{ele['name']} has birthday today, Email is sent")
    else:
        print(f"{ele['name']} has no birthday today")
