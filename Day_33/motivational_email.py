import datetime as dt
import smtplib
import random
my_email ="maheshmj200@gmail.com"
password = "********************************"

#now =dt.datetime.today().strftime('%A')

weekday =dt.datetime.today().weekday()

if weekday== 0:
    with open("Day_33\quotes.txt","r") as f:
        data=f.readlines()
        
    random_quote = random.choice(data)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # To keep connection is sure, It will encrypt the email address
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation \n\n {random_quote}")
else:
    print("its not Monday")
    

