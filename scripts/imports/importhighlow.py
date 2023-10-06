# TODO Pull data from finance using yfinance

import yfinance as yf
import indexlist as inxlst
import pandas as pd

start_date = '2018-01-01' 
end_date = '2023-04-28' 

# More general reusable stuff
symlst = inxlst.spinx
initial = yf.download(symlst[0], start_date, end_date)
initial[symlst[0] + 'high'] = initial.High
initial[symlst[0] + 'low'] = initial.Low

highlow= initial[[symlst[0]  + 'high', symlst[0]  + 'low']]

# Makes merged table of highs and lows
for sym in symlst[1:]: 
  data = yf.download(sym, start_date, end_date)
  # data['AdvDec'] = 1 if (data.High - data.Low) > 0 else -1
  data[sym + 'high'] = data.High
  data[sym + 'low'] = data.Low
  highlow = pd.merge(highlow, data[[sym + 'high', sym + 'low']], how='inner', on="Date")

print(highlow.describe())

# tempdata = pd.merge(dllst[0][["High", "Low"]], dllst[1][["High", "Low"]], suffixes=(symlst[0], symlst[1]),how='inner', on="Date")
# tempdata = pd.merge(tempdata, dllst[2][["High", "Low"]],suffixes=("", symlst[2]), how='inner',  on="Date")
# # tempdata = pd.concat(dllst)
# print(tempdata)
highlow.to_csv("first3highlow.csv")

# data = pd.read_csv("first3.csv")

symbol = 'AAPL' 

# /*Loads data in a dataframe
# Maybe cache the results in the future */

# data = yf.download(symbol, start=start_date, end=end_date)

# print(data.describe())
# print(data.head())
# %matplotlib widget

# print(list(data.columns))
# print(data.index)
# print(data[['Low','High']])

# Culm positive vs negative

# lows = data['Low']
# highs = data['High']
# dates = data.index


# fig, (ax0) = plt.subplots(1, 1, sharex=True, constrained_layout=True)
# # # Price:
# ax0.plot(dates, lows, label='Low Price')
# ax0.plot(dates, highs, label='High Price')
# ax0.legend(loc='upper right')
# ax0.set_ylabel('Ticker Prices $') 
# ax0.set_title('AAPL stock price', loc='left')

# TODO Make all the summmary subplots 
# TODO Make an overall score
# TODO Make some comparisons in other areas

# TODO Host the results of the webpage. 


print(fig)