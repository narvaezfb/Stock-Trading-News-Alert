import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STOCKS_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def FetchDailyStockInformation():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def GetYesterdaysDate(todaysDate: dt.datetime) -> dt.datetime:
    return todaysDate - dt.timedelta(days=1)


def GetDayBeforeYesterdayDate(todaysDate: dt.datetime) -> dt.datetime:
    return todaysDate - dt.timedelta(days=2)


def FormatDateToYearMonthDay(date: dt.datetime) -> str:
    return date.strftime("%Y-%m-%d")


def GetStockValueByDate(date: dt.datetime, data) -> float:
    return float(data["Time Series (Daily)"][date]["4. close"])


def CalculateTwoStocksPercentageDifference(firstStockValue: float, secondStockValue: float) -> float:
    return (firstStockValue - secondStockValue) / \
        ((firstStockValue + secondStockValue)/2) * 100


def CheckIfStockPricesIncreasedOrDecreasedByFivePercent(firstStockValue: float, secondStockValue: float) -> bool:
    percentageDifference = CalculateTwoStocksPercentageDifference(
        firstStockValue, secondStockValue)
    return percentageDifference > 5
