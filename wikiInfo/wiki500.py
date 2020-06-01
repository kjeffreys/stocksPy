'''
@file: wiki500.py File for getting, storing, and transporting data about S&P 500 stock info
@author: Kyle Jeffreys
'''
import bs4 as bs
import pickle
import requests
import json

'''
Method to return tickers from local pickle file without executing wiki query/parsing.
'''
def getWiki500():

    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    return tickers

'''
Method to read JSON version of tickers file
'''
def getJSON500():

    with open("sp500tickers.json", "r") as f:
        tickers = json.load(f)

    return sorted(tickers)

'''
Method that will both update the indices files and return the index tickers
'''
def updateWiki500():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker.rstrip())

    with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)

    return tickers

'''
Writing to JSON file instead
'''
def updateWiki500JSON():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker.rstrip())

    with open("sp500tickers.json", "w") as f:
            json.dump(tickers, f)

    #return tickers

if __name__ == '__main__':
    print("\nUpdating tickers...")
    tickersOne = updateWiki500() # use if file needs update
    tickersTwo = getWiki500()
    print(tickersOne) #use if file needs update
    print("\nGetting tickers from ticker pickle file")
    print(tickersTwo)
    print("\nSorting...")
    print(sorted(tickersTwo))
    updateWiki500JSON()
    print()
    print(getJSON500())
