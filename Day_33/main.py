import smtplib

my_email ="maheshmj200@gmail.com"
password = "*************"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # To keep connection is sure, It will encrypt the email address
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="mjack855@gmai.com",
                        msg="Subject:hello \n\n hello world")

import datetime as dt

now=dt.datetime.now()
year =now.year
day =now.day
date_of_birth = dt.datetime(year=1995,month=2,day=4)
print(date_of_birth)

#cofp wvte idav izto