API_KEY ="14291dd47b288f9864f55737698edd37"
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'AC5c0799de2766fd8d6a680d452a13181a'
auth_token = '6d24181aeab782ae5a9e4c05769af1cc'
import requests
from twilio.rest import Client
client = Client(account_sid, auth_token)


weather_paramas ={
    "lat":31.596554,
    "lon":130.557114,
    "appid":API_KEY,
    "cnt":4
}

response = requests.get(url=OWM_ENDPOINT,params=weather_paramas)
response.raise_for_status()
data = response.json()
will_rain = False
for ele in data['list']:
    condition_code =ele['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages.create(
                from_='+12674690821',
                body='Its going to rain',
                to='+918867827084'
            )
   print(message.status)
