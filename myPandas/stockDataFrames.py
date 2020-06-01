import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web
from pandas import Series, DataFrame
import alpaca_trade_api as tradeapi

# TODO: Take list of stock tickers
# TODO: Query API for data
# TODO: Map data into pandas DataFrame with {k,v} of {ticker, data}

'''
Query that demonstrates a simple use of Pandas dataframe reading
Key is set to date...
Also can edit date for a start and end range with days in between at a rate such as each day
'''
def exampleQuery():
    print("Example Query-----------------------------")
    start = datetime(2020,5,6)
    end = datetime(2020,5,6)
    df = web.DataReader("BA", 'yahoo', start, end)
    print(df.tail())

def get5Y():
    print("Five Year-----------------------------")
    date = datetime.today()
    fiveYearDelta = date - relativedelta(years=5)

    if fiveYearDelta.weekday() == 5:
        fiveYearDelta = fiveYearDelta - relativedelta(days=1)

    elif fiveYearDelta.weekday() == 6:
        fiveYearDelta = fiveYearDelta - relativedelta(days=2)

    print(fiveYearDelta)
    dateStr = fiveYearDelta.strftime("%Y-%m-%d")
    #date2 = fiveYearDelta + relativedelta(days=1)
    #if date2.weekday() == 5:
    #    fiveYearDelta = date2 + relativedelta(days=2)
    #elif fiveYearDelta.weekday() == 6:
    #    fiveYearDelta = date2 + relativedelta(days=1)
    #print("\n" + str(date2))
    #dateStr2 = date2.strftime("%Y-%m-%d")

    #df2 = web.DataReader("BA", 'yahoo', fiveYearDelta, date2)
    #print(df2.tail())

    return dateStr

def get1Y():
    print("One Year-----------------------------")
    date = datetime.today()
    oneYearDelta = date - relativedelta(years=1)

    if oneYearDelta.weekday() == 5:
        oneYearDelta = oneYearDelta - relativedelta(days=1)

    elif oneYearDelta.weekday() == 6:
        oneYearDelta = oneYearDelta - relativedelta(days=2)

    print(oneYearDelta)
    dateStr = oneYearDelta.strftime("%Y-%m-%d")
    #date2 = oneYearDelta + relativedelta(days=1)
    #if date2.weekday() == 5:
    #    oneYearDelta = date2 + relativedelta(days=2)
    #elif oneYearDelta.weekday() == 6:
    #    oneYearDelta = date2 + relativedelta(days=1)
    #print("\n" + str(date2))
    #dateStr2 = date2.strftime("%Y,%m,%d")

    #df2 = web.DataReader("BA", 'yahoo', oneYearDelta, date2)
    #print(df2['High'])
    #print(df2.tail())
    return dateStr

def get1D():
    print("One Day-----------------------------")
    date = datetime.today()
    oneDayDelta = date - relativedelta(days=1)

    if oneDayDelta.weekday() == 5:
        oneDayDelta = oneDayDelta - relativedelta(days=1)

    elif oneDayDelta.weekday() == 6:
        oneDayDelta = oneDayDelta - relativedelta(days=2)

    print(oneDayDelta)
    dateStr = oneDayDelta.strftime("%Y-%m-%d")
    #date2 = oneDayDelta + relativedelta(days=1)
    #if date2.weekday() == 5:
    #    oneDayDelta = date2 + relativedelta(days=2)
    #elif oneDayDelta.weekday() == 6:
    #    oneDayDelta = date2 + relativedelta(days=1)
    #print("\n" + str(date2))
    #dateStr2 = date2.strftime("%Y,%m,%d")

    #df2 = web.DataReader("BA", 'yahoo', oneDayDelta, date2)
    #print(df2['High'])
    #print(df2.tail())
    return dateStr


def demoDateStringMethods():
    print("demoDateStringMethods-----------------------------")
    date = datetime.today()
    print("date = datetime.datetime.today(): {}".format(date))
    date2 = date + relativedelta(days=3)
    print("date = datetime.datetime.today(): {}".format(date2))
    print("date2.weekday(): {}".format(date2.weekday())) # prints 0-6...M-Sun
    print("date2.strftime(\"%A\"): {}".format(date2.strftime("%A"))) # Formats day of Week as Monday, Tuesday, etc for current day of datetime object
    date3 = date2 - relativedelta(years=5)
    print("date3 = date2 - relativedelta(years=5)")
    print("date3.weekday(): {}".format(date3.weekday()))   

if __name__ == '__main__':
    exampleQuery()
    get5Y()
    get1Y()
    demoDateStringMethods()