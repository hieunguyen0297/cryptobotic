# Press F1 -> type run -> find run Python file -> set ketbinding
# Press Shift + R to run the file
# Navigate to the folder that contain the python file type python + file.py


import ccxt

hitbtc   = ccxt.hitbtc({'verbose': True})
bitmex   = ccxt.bitmex()
huobipro = ccxt.huobipro()
binance  = ccxt.binance()


print(bitmex.fetch_balance())

# hitbtc_markets = hitbtc.load_markets()

tickers = huobipro.fetch_ticker('ETH/HUSD')
eth_low = bitmex.fetch_ticker('ETH/USD')['low']
eth_close = bitmex.fetch_ticker('ETH/USD')['close']


# print(tickers)


# print(eth_low)
# print(eth_close)
# print(huobipro.fetch_trades('LTC/USDT'))

