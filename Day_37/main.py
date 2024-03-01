STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import datetime as dt

def percent_change(old, new):
     pc = round((new - old) / abs(old) * 100, 2)
     return pc

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = ('https://www.alphavantage.co/query?'
       'function=TIME_SERIES_DAILY&'
       'symbol=TSLA'
       '&apikey=NPRHBXKY5LOQA1DQ')
stock_trading_rate = requests.get(url)
stock_trading_rate.raise_for_status()
data = stock_trading_rate.json()
today = dt.date.today()
yesterday= today-dt.timedelta(days=1)
day_before_yes = today-dt.timedelta(days=2)
cool=data['Time Series (Daily)']
print(percent_change(float(data['Time Series (Daily)'].get(str(today-dt.timedelta(days=2))).get('4. close')),float(cool.get(str(yesterday)).get('4. close'))))


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

