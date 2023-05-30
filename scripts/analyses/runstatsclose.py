# TODO Create analyses with numpy etc

import importlib.util
import sys,os
import yfinance as yf
# from .scripts.imports import spinx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functools

ticksymlst = ["MMM",
         'AOS',
         'ABT',]

closedata = pd.read_csv("first3close.csv")
# TODO: Create CloseData that's all of the required tables put together. 


# testvalue = closedata.at["2018-01-02", "AOSclose"]

# calcAdvDec calculates Advance and decline for inx (a data frameindex) and ticksym (stock ticker symbol)
# returns if the stock advanced, declined or remained the same that day
def calcAdvDec (inx):
    sumadvdec = 0
    for ticksym in ticksymlst:
      if closedata.at[inx, ticksym+"open"] - closedata.at[inx, ticksym+"close"] > 0:
          sumadvdec += 1
      elif closedata.at[inx, ticksym+"open"] - closedata.at[inx, ticksym+"close"] == 0:
          continue
      else:
          sumadvdec -= 1
    return sumadvdec


# returns the series of cumulative advance and declines
def allAdvDec(x):
    return sum 

closedata = closedata.set_index("Date")
testvalues = closedata.index
closedata["AdvDec"] = list(map(calcAdvDec, testvalues))



print(closedata)

# The Formula for Advance/Decline (A/D) Line Is:
# A/D = Net Advances  +  { PA, if PA value exists else 0
# where:
# Net Advances == Difference between number of daily ascending and declining stocks 
#  PA == Previous Advances == Prior indicator reading
# ​
