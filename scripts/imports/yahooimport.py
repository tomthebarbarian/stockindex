# TODO Pull data from finance using yfinance

import yfinance as yf

import numpy as np

import matplotlib.pyplot as plt

symbol = 'AAPL' 
start_date = '2018-01-01' 
end_date = '2023-04-28' 

# Loads data in a dataframe
# Maybe cache the results in the future
data = yf.download(symbol, start=start_date, end=end_date)

# print(data.describe())
# print(data.head())
# %matplotlib widget

# print(list(data.columns))
# print(data.index)
# print(data[['Low','High']])


lows = data['Low']
highs = data['High']
dates = data.index


fig, (ax0) = plt.subplots(1, 1, sharex=True, constrained_layout=True)
# # Price:
ax0.plot(dates, lows, label='Low Price')
ax0.plot(dates, highs, label='High Price')
ax0.legend(loc='upper right')
ax0.set_ylabel('Ticker Prices $') 
ax0.set_title('AAPL stock price', loc='left')

# TODO Make all the summmary subplots 
# TODO Make an overall score
# TODO Make some comparisons in other areas

# TODO Host the results of the webpage. 


print(fig)