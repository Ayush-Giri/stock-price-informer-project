import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_trading_api_key = "N32WOYFVKA4AU97W"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_trading_api_key
}


response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
closing_price_yesterday = data["Time Series (Daily)"]["2021-07-01"]["4. close"] # Adjust date according to your requirement
closing_price_day_before_yesterday = data["Time Series (Daily)"]["2021-06-30"]["4. close"] # Adjust date according to your requirement


difference = float(closing_price_day_before_yesterday) - float(closing_price_yesterday)
difference_in_percentage = (difference/float(closing_price_yesterday)) * 100


if difference_in_percentage > 5 or difference_in_percentage < -5:
    news_api_key = "e420a1e7bb314f8ba6b1feb58bb372d6"
    news_parameters = {
        "q": "tesla",
        "apiKey": news_api_key

    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    final_news_data = news_data["articles"][:3]

    account_sid = "ACf1ba52d3ac06694341734af3126b2fc0"
    auth_token = "e8305ad2fa650ff8ec62ca3b5ba0d8a4"
    client = Client(account_sid, auth_token)
    for news in final_news_data:
        message = client.messages.create(
            body = news,
            from_='+15017122661',
            to='+9779814358733'
    )
        print(message.status)

