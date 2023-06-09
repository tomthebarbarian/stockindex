# TODO Pull data from finance using yfinance

import yfinance as yf
import indexlist as inxlst
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_date = '2018-01-01' 
end_date = '2023-04-28' 

# More general reusable stuff
spdata = pd.read_csv("data/SPTickerWiki.csv")
symlst = spdata['Symbol']

# symlst = inxlst.spinx
initial = yf.download(symlst[0], start_date, end_date)
initial[symlst[0] + 'close'] = initial.Close
initial[symlst[0] + 'open'] = initial.Open

close= initial[[symlst[0]  + 'close', symlst[0]  + 'open']]

# Makes merged table of close
for sym in symlst[1:]: 
  data = yf.download(sym, start_date, end_date)
  # data['AdvDec'] = 1 if (data.High - data.Low) > 0 else -1
  data[sym + 'close'] = data.Close
  data[sym + 'open'] = data.Open
  close = pd.merge(close, data[[sym + 'close', sym + 'open']], how='inner', on="Date")

print(close.describe())

close.to_csv("500close.csv")
