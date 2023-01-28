import os
from dotenv import load_dotenv
import requests
import datetime as dt


load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2022-12-28&sortBy=publishedAt&apiKey={API_KEY}"


def FetchRecentArticlesOfTesla():
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def GetFirstThreeNewsFromTeslaNewsResponse(data):
    return data['articles'][:3]


def PrepareDataInNiceFormat(threeArticles):
    smsText = ""
    index = 1
    for article in threeArticles:
        smsText += f"#{index} - "
        smsText += article['title']
        smsText += "\n\n"
        smsText += article['description']
        smsText += "\n\n"
        index += 1

    return smsText
