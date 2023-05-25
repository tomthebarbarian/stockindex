# TODO Pull data from finance using yfinance

import yfinance as yf
import indexlist as inxlst
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_date = '2018-01-01' 
end_date = '2023-04-28' 

# More general reusable stuff
symlst = inxlst.spinx
initial = yf.download(symlst[0], start_date, end_date)
initial[symlst[0] + 'close'] = initial.Close

close= initial[[symlst[0]  + 'close']]

# Makes merged table of close
for sym in symlst[1:]: 
  data = yf.download(sym, start_date, end_date)
  # data['AdvDec'] = 1 if (data.High - data.Low) > 0 else -1
  data[sym + 'close'] = data.High
  close = pd.merge(close, data[[sym + 'close']], how='inner', on="Date")

print(close.describe())

# tempdata = pd.merge(dllst[0][["High", "Low"]], dllst[1][["High", "Low"]], suffixes=(symlst[0], symlst[1]),how='inner', on="Date")
# tempdata = pd.merge(tempdata, dllst[2][["High", "Low"]],suffixes=("", symlst[2]), how='inner',  on="Date")
# # tempdata = pd.concat(dllst)
# print(tempdata)
close.to_csv("first3close.csv")
