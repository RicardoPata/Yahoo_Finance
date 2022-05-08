import yfinance as yf
from datetime import datetime
import time

# function to get yahoo stock price . Pre-market and market. 
Ticker = str(input(" write your ticker: "))

def yfPrice(stock):
    
    today = datetime.now()

    bfri = yf.Ticker(stock)
    MarketPrice = bfri.info["regularMarketPrice"]
    PreMarketPrice = bfri.info["preMarketPrice"]

    PrecoLive = str('\n {} \n Pre market price: {} \n Market price: {} \n  \n \n').format(today, PreMarketPrice, MarketPrice)
    print(PrecoLive)

    time.sleep(5)

while True:
    yfPrice(Ticker)
