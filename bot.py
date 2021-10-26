# Press F1 -> type run -> find run Python file -> set ketbinding
# Press Shift + R to run the file
# Navigate to the folder that contain the python file type python + file.py
# This version currently does not support for trading in real time market
# It only work with JavaScript version

import pandas as pd
import mplfinance as mpf
import numpy as np
import ccxt
from datetime import datetime
import time
import configparser
import matplotlib

config = configparser.ConfigParser()
config.read('config.ini')

exchange_id = 'binanceus'
exchange_class = getattr(ccxt, exchange_id)

# Use 1 for your trading preferences, use 2 for analytic

# 1
# binance = exchange_class({
#     'apiKey': YOUR_API_KEY,
#     'secret': YOUR_SECRET_KEY,
    
# })

# 2
binance = ccxt.binance()
  

def order():
    # use fetchOHLCV to get price for the crypto
    price = binance.fetchOHLCV("ETH/USDT", "1m", since=None, limit=6)
    
    # re-format the output
    format_price = []
    for arr in price:
        dic = {
            "timestamp": datetime.fromtimestamp(arr[0] / 1000).strftime('%d-%m-%Y, %H:%M:%S'),
            "open": arr[1], 
            "high": arr[2], 
            "low": arr[3], 
            "close": arr[4], 
            "volume": arr[5] 
        }
        format_price.append(dic)
    
    # data for each bar on "1m" timeframe
    # [
    #     {'open': 62193.15, 'high': 63732.39, 'low': 60000.0, 'close': 60688.22, 'volume': 52119.35886}, 
    #     {'open': 60688.23, 'high': 61747.64, 'low': 59562.15, 'close': 61286.75, 'volume': 27626.93678},
    #     {'open': 61286.75, 'high': 61500.0, 'low': 59510.63, 'close': 60180.01, 'volume': 22095.03978}
    # ]
    
    # for price in format_price:
    #     print(price['close'], sep = '\n')
           
           
           
    direction = ''    
    #Get average Price for the last 5 sticks
    average_price = 0
    sum_price = 0
    
    # Get last price
    last_price = format_price[len(format_price) - 1]['close']
    
    # Loop through the array for price to get sum
    for item in format_price:
       sum_price += item['close']
        
    average_price = sum_price / len(format_price)    
     
    if last_price > average_price:
        direction = 'sell'
    else:
        direction = 'buy'
     
    # Amount of money want to trade
    money = 10 
    
    # Number of shares/coins
    quantity = money / last_price
    
    # Make market order
    # Currently don't support
    # binance.create_market_order("ETH/USD", direction, quantity)

    # Print 6 recent candle sticks
    print(price)



def show_chart():
    # Make a data frame to plug in the chart
    # Fetch all in record
    fetch_not_limit = binance.fetchOHLCV("ETH/USDT", "1m")  
    df = pd.DataFrame(np.array(fetch_not_limit), columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    # df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    df.index = pd.DatetimeIndex(df['timestamp'])
    # Plug in the chart 
    
    mpf.plot(df,type='candle', mav=(20,50,100),title='ETHUSD', style='yahoo', volume=True,block=False)
    mpf.show()
    print(df)


def main():
    # show interactive chart here before enter the trade  
    show_chart()  
    # The bot continue until stop
    while True:
        order() 
        print("I'm sleeping for under a mintutes. Just wait please!")
        time.sleep(10)

main()
