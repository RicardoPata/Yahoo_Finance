import yfinance as yf
from datetime import datetime
import time

# function to get yahoo stock price . Pre-market and market. 
Ticker = str(input(" write your ticker: "))

def yfPrice(stock):
    
    today = datetime.now()

    Stock = yf.Ticker(stock)
    MarketPrice = Stock.info["regularMarketPrice"]
    PreMarketPrice = Stock.info["preMarketPrice"]

    LivePrice = str('\n {} \n Pre market price: {} \n Market price: {} \n  \n \n').format(today, PreMarketPrice, MarketPrice)
    print(LivePrice)

    time.sleep(5)

while True:
    yfPrice(Ticker)
