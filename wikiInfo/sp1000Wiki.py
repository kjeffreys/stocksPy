'''
@file: sp1000Wiki.py File for getting, storing, and transporting data about S&P 1000 stock info
@author: Kyle Jeffreys
'''
import bs4 as bs
import pickle
import requests
import json

'''
Method to return tickers from local pickle file without executing wiki query/parsing.
'''
def getWiki1000():

    with open("sp1000tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    return tickers

'''
Method to read JSON version of tickers file
'''
def getJSON1000():

    with open("sp1000tickers.json", "r") as f:
        tickers = json.load(f)

    return tickers

'''
Method that will both update the indices files and return the index tickers
'''
def updateWiki1000():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_1000_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker.rstrip())

    with open("sp1000tickers.pickle", "wb") as f:
        pickle.dump(sorted(tickers), f)

    return tickers

'''
Writing to JSON file instead
'''
def updateWiki1000JSON():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_1000_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker.rstrip())

    with open("sp1000tickers.json", "w") as f:
        json.dump(sorted(tickers), f)

    # return tickers
'''
Updates pickle file with sp1000 tickers and sector info from wikipedia.
'''
def nameSectorIndustry():
    tickers = getWiki1000()
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_1000_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickerNSI = []
    
    for row in table.findAll('tr')[1:]:
        name = row.findAll('td')[0].text.rstrip()
        economicSector = row.findAll('td')[2].text.rstrip()
        subIndustry = row.findAll('td')[3].text.rstrip()
        tickerNSI.append([name, economicSector,subIndustry])

    with open("sp1000tickerNSI.pickle", "wb") as f:
        pickle.dump(tickerNSI, f)

'''
Gets info from local pickle file about sp1000 tickers and sector info.
'''
def getNameSectorIndustry():

    with open("sp1000tickerNSI.pickle", "rb") as f:
        tickerNSI = pickle.load(f)

    return tickerNSI




if __name__ == '__main__':
    print("\nUpdating tickers...")
    tickersOne = updateWiki1000()
    tickersTwo = getWiki1000()
    print(tickersOne)
    print("\nGetting tickers from ticker pickle file")
    print(tickersTwo)
    nameSectorIndustry()
    print(getNameSectorIndustry())
    updateWiki1000JSON()
    print()
    print(getJSON1000())
    
