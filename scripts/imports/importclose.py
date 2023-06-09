# TODO Pull data from finance using yfinance

import yfinance as yf
import pandas as pd
import dask

start_date = '2023-01-01' 
end_date = '2023-04-28' 

# More general reusable stuff
spdata = pd.read_csv("data/SPTickerWiki.csv")
symlst = spdata['Symbol']

initial = yf.download(symlst[0], start_date, end_date)
initial[symlst[0] + 'close'] = initial.Close
initial[symlst[0] + 'open'] = initial.Open

close= initial[[symlst[0]  + 'close', symlst[0]  + 'open']]

# Makes merged table of close
# data['AdvDec'] = 1 if (data.High - data.Low) > 0 else -1

failedLst = []

for sym in symlst[1:]: 
  try: 
    data = yf.download(sym, start_date, end_date)
    data[sym + 'close'] = data.Close
    data[sym + 'open'] = data.Open
    close = pd.merge(close, data[[sym + 'close', sym + 'open']], how='inner', on="Date")
  except:
    failedLst = failedLst + [sym]
    continue


# close = pd.merge(close, data[[sym + 'close', sym + 'open']], how='inner', on="Date")

missingdata = pd.DataFrame(data={'failedDL':failedLst})
missingdata.to_csv("results/failedDLclose.csv")
close.to_csv("results/500close.csv")
