import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "NQROFRBCPVRTT2HI"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "46dda36314244d60829f9cf8afa23e33"
STOCK_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}"
CLOSE = "4. close"

ACCOUNT_SID = 'get your own'
AUTH_TOKEN = 'get your own'

stock_response = requests.get(STOCK_URL)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [date for (date, value) in stock_data.items()]

yesterday = stock_data_list[0]
yesterday_closing_price = stock_data[yesterday][CLOSE]

day_before_yesterday = stock_data_list[1]
day_before_yesterday_closing_price = stock_data[day_before_yesterday][CLOSE]

difference = float(day_before_yesterday_closing_price) - float(yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 3:
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "to": day_before_yesterday,
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    first_three_articles = articles[:3]

    formatted_articles_list = [f"{STOCK}:{up_down}{diff_percent}% \nHeadline: {article['title']}. \nLink to the article: {article['url']}" for article in first_three_articles]

    for article in formatted_articles_list:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=article,
            from_="+17086690263",
            to="+your number"
        )
print(message.status)

