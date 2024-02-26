import requests
import datetime as dt

response=requests.get(url='http://api.open-notify.org/iss-now.json') #fetch the data from endpoint
response.raise_for_status()
data=response. json()
longitude=data['iss_position']['longitude']
latitude=data['iss_position']['latitude']
parameters={
    "lat": latitude,
    "lng": longitude,
    "formatted": 0
}

request_sunset = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
request_sunset.raise_for_status()
data=request_sunset.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
today =dt.datetime.today()
hour=today.hour
print(sunrise)
print(hour)