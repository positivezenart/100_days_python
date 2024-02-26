import requests
import datetime as dt
import smtplib

MY_LAT=12.295810
MY_LANG =76.639381
MY_EMAIL ="maheshmj200@gmail.com"
PASSWORD = "cofpwvteidavizto"

def iss_over_head():
    global longitude,latitude
    response=requests.get(url='http://api.open-notify.org/iss-now.json') #fetch the data from endpoint
    response.raise_for_status()
    data=response. json()
    longitude=float(data['iss_position']['longitude'])
    latitude=float(data['iss_position']['latitude'])

    if MY_LAT - 5 <= latitude <= MY_LAT+5 and MY_LANG - 5 <= longitude <= MY_LANG +5:
      return True

def is_it_night():
    parameters={
        "lat": MY_LAT,
        "lng": MY_LANG,
        "formatted": 0
     }
    
    request_sunset = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    request_sunset.raise_for_status()
    data=request_sunset.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    today =dt.datetime.now()
    current_hour=today.hour

    if current_hour>=sunset or current_hour <= sunrise:
        return True
    
if iss_over_head():
    if is_it_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # To keep connection is sure, It will encrypt the email address
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Lucky Day, ISSover head\n\n Hey Due, Go outside and check ISS over your head at clear sky!")
        
else:
    print("Go back to sleep mode")