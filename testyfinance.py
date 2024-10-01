# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import yfinance as yf 
data = yf.download(["MSFT"], period="6mo")

temp = yf.download(["MSFT"], period="6mo")


# from yahoofinancials import YahooFinancials
# yf = YahooFinancials("MSFT")
# data = yf.get_historical_price_data("2024-01-01","2024-05-01", "daily")


from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='NX3XKPQHG5Z1EA7J')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='USD',to_currency='INR')





from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='NX3XKPQHG5Z1EA7J', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()




import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']


async def get_data(symbol):
    ts = TimeSeries(key='NX3XKPQHG5Z1EA7J')
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data

loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
loop.close()