# TODO Create analyses with numpy etc
import sys,os
# from .scripts.imports import spinx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', '..', 'data')
sys.path.append( mymodule_dir )

# TODO:
# For each of the 11 sp 500 sectors
# Calculate the percentage of stocks per sector that fullfil the following:
# Have a higher closing price than the respective 20 day simple moving average

# Sum the percentages for the 11 sectors for a score out of 1100
# Colour it bullish if score is <200, and bearish if >1000

# TODO: Should probably make a bargraph comparing the percentages and donut chart of the biggest contributors to low/high scores

spdata = pd.read_csv("data/SPTickerWiki.csv")
columnnames = spdata.columns
GICSSectors = spdata['GICS Sector'].unique()
databysector = {}

# Create lists by sector
for sector in GICSSectors:
    databysector[sector] = [spdata['Symbol'][spdata['GICS Sector'] == sector]]

for sym in symlst[1:]: 
  try: 
    data = yf.download(sym, start_date, end_date)
    data[sym + 'close'] = data.Close
    data[sym + 'open'] = data.Open
    close = pd.merge(close, data[[sym + 'close', sym + 'open']], how='inner', on="Date")
  except:
    failedLst = failedLst + [sym]
    continue

def calcAdvDec (inx):
    sumadvdec = 0
    for ticksym in ticksymlst:
      if closedata.at[inx, ticksym+"open"] - closedata.at[inx, ticksym+"close"] > 0:
          sumadvdec -= 1
      elif closedata.at[inx, ticksym+"open"] - closedata.at[inx, ticksym+"close"] == 0:
          continue
      else:
          sumadvdec += 1
    return sumadvdec



print(databysector)