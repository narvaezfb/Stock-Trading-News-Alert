from stocks import *
from news import *
from sms import *
import datetime as dt


def main():
    # Fetch Data
    data = FetchDailyStockInformation()

    # Get Today's Date
    todaysDate = dt.datetime.now()
    # Get yesterdays Date
    yesterdaysDate = FormatDateToYearMonthDay(GetYesterdaysDate(todaysDate))
    # Get Day Before Yesterday Date
    dayBeforeYesterdayDate = FormatDateToYearMonthDay(
        GetDayBeforeYesterdayDate(todaysDate))

    # Get Stock Values from Dates
    yesterdayStockValue = GetStockValueByDate(yesterdaysDate, data)
    dayBeforeStockValue = GetStockValueByDate(dayBeforeYesterdayDate, data)

    if CheckIfStockPricesIncreasedOrDecreasedByFivePercent(yesterdayStockValue, dayBeforeStockValue):
        teslaNews = FetchRecentArticlesOfTesla()
        latestThreeArticles = GetFirstThreeNewsFromTeslaNewsResponse(teslaNews)
        formattedData = PrepareDataInNiceFormat(latestThreeArticles)
        SendSMS(formattedData)


main()
