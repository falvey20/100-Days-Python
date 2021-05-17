import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "" #AlphaVantage
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "" #NewsAPI

stock_response = requests.get(f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={STOCK_API_KEY}")
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
day_before_yesterday = data_list[1]
day_before_closing = day_before_yesterday["4. close"]

difference = float(yesterday_closing) - float(day_before_closing)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference)

diff_percent = round((difference / float(yesterday_closing)) * 100)
print(diff_percent)

if abs(diff_percent) >= 2:

    news_response = requests.get(f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}")
    news_articles = news_response.json()["articles"]
    first_3_articles = news_articles[:3]

    account_sid = "" #TwilioTrial
    auth_token = "" #TwilioTrial
    client = Client(account_sid, auth_token)

    for article in first_3_articles:
        title = article["title"]
        description = article["description"]
        message = client.messages \
            .create(
            body=f"{STOCK}: {up_down}{diff_percent}\nHeadline: {title}\nBrief: {description}",
            from_='', # TwilioNo.
            to='' # TestNo.
        )

        print(message.status)
