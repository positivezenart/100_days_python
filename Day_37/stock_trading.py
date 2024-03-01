import requests
from twilio.rest import Client
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
account_sid = 'AC5c0799de2766fd8d6a680d452a13181a'
auth_token = '6d24181aeab782ae5a9e4c05769af1cc'
today = dt.date.today()

def percent_change(old, new):
     pc = round((new - old) / abs(old) * 100, 2)
     return pc

#Selecting a last two days trading closing price, finding the change in percentage
stock_url = ('https://www.alphavantage.co/query?'
       'function=TIME_SERIES_DAILY&'
       'symbol=TSLA'
       '&apikey=NPRHBXKY5LOQA1DQ')

stock_trading_rate = requests.get(stock_url)
stock_trading_rate.raise_for_status()
data = stock_trading_rate.json()
stock_data =data['Time Series (Daily)']
variation_in_percentage = percent_change(float(stock_data.get(str(today-dt.timedelta(days=2))).get('4. close')),float(stock_data.get(str(today-dt.timedelta(days=1))).get('4. close')))

print(f"Variation in stock comapred to yesterday is {variation_in_percentage} ")


#selecting the news about this company based on popularity
url = ('https://newsapi.org/v2/everything?'
       'q=Tesla&'
       'searchIn=title&'
       'from=2024-02-24&'
       'language=en&'
       'pageSize=1&'
       'sortBy=popularity&'
       'apiKey=138dbe996d7f462296b01869f94bd428')

response_news = requests.get(url)
response_news.raise_for_status()
news_data = response_news.json()
title = [ele['title'] for ele in news_data['articles']]
brief = [ele['description'] for ele in news_data['articles']]

#sending an sms to client
client = Client(account_sid, auth_token)
message = client.messages.create(
                from_='+12674690821',
                body=f"{COMPANY_NAME}: {variation_in_percentage}, Headline:{title},brief:{brief}",
                to='+918867827084'
            )
print(message.status)
