from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()


def get_news() -> list:
    news_params = {
        "apiKey": os.environ.get("NEWS_API_KEY"),
        "searchIn": "title,description",
        "language": "en",
        "q": f"{STOCK} OR {COMPANY_NAME}",
    }
    return [
        (article["title"], article["description"])
        for article in make_request(
            url="https://newsapi.org/v2/everything", params=news_params
        )["articles"][:3]
    ]


def make_request(url: str, params: dict) -> dict:
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def get_price_difference():
    def format_article_body(article: tuple, percent_price_change: float):
        if percent_price_change < 0:
            directional_sign = "🔻"
        else:
            directional_sign = "🔺"
        return f"""
        {STOCK}: {directional_sign}{round(percent_price_change * 100)}%
        Headline: {article[0]}
        Brief: {article[1]}
        """

    alphavantage_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.environ.get("ALPHAVANTAGE_API_KEY"),
    }
    alphavantage_returned = make_request(
        url="https://www.alphavantage.co/query", params=alphavantage_params
    )

    time_series = alphavantage_returned["Time Series (Daily)"]
    price_past_two_days = [time_series[day] for day in list(time_series.keys())[1:3]]

    def get_close_price(time_series_point: dict) -> float:
        return float(time_series_point["4. close"])

    yesterday_close_prince = get_close_price(price_past_two_days[0])
    two_days_ago_close_prince = get_close_price(price_past_two_days[1])
    percent_price_change = (
        yesterday_close_prince - two_days_ago_close_prince
    ) / two_days_ago_close_prince

    if abs(percent_price_change) > 0.05:
        client = Client(
            os.environ["TWILLIO_ACCOUNT_SID"], os.environ["TWILLIO_AUTH_TOKEN"]
        )
        articles = get_news()
        for article in articles:
            message = client.messages.create(
                body=format_article_body(article, percent_price_change),
                from_=os.environ["TWILLIO_PHONE_NUMBER"],
                to=os.environ["MY_PHONE_NUMBER"],
            )
            print(message.status)
