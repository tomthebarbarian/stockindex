# TODO Create analyses with numpy etc
import sys,os
# from .scripts.imports import spinx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from sqlalchemy import create_engine
import psycopg2

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', '..', 'data')
mymodule_dir = os.path.join( script_dir, '..', '..', 'results')
sys.path.append( mymodule_dir )


from datetime import datetime, timedelta


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
# closeData = pd.read_csv("results/500close.csv")


alchemyEngine   = create_engine('postgresql+psycopg2://test:@127.0.0.1:5432/stockindex', pool_recycle=3600)
dbConnection    = alchemyEngine.connect()
closeData       = pd.read_sql("select * from \"spclose\"", dbConnection)
pd.set_option('display.expand_frame_repr', False)

# closeData = closeData.set_index("Date")

# Date Format YYYY-MM-DD
today = datetime.today()
# end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
# end_date = '2023-08-04'
end_date = datetime.strptime('2023-08-04', '%Y-%m-%d').date()

# 
sumPercAdvDec = 0
advDecPerSector = []
# Create lists by sector
for sector in GICSSectors:
  databysector[sector] = spdata[(spdata['GICS Sector'] == sector)]['Symbol']
# Calc moving average and if close price is higher for the data add 1 to sector advdec
# Select by column heads
  sectorAdvDec = 0
  # print(databysector[sector])
  for sym in databysector[sector]: 
    colname = sym + "close"
    valatloc = closeData[(closeData["Date"] == end_date)][colname].values[0]
    if np.mean(closeData[colname]) < valatloc:
       sectorAdvDec += 1
    print(sectorAdvDec, sym)
  if sectorAdvDec < 0:
     sectorAdvDec = 0
  else:
     sectorAdvDec = (sectorAdvDec*100)/databysector[sector].size
  print(sectorAdvDec, sector)
  sumPercAdvDec += sectorAdvDec
  advDecPerSector += [sector, sectorAdvDec]

print(sumPercAdvDec)

