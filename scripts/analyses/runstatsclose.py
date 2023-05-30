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


closedata = closedata.set_index("Date")
testvalues = closedata.index


# This caculates culmulative advance decline
i = 0
anslist = []
immlist = []
while i < len(list(testvalues)):
    if i > 0:
      anslist = anslist + [anslist[i-1] + calcAdvDec(testvalues[i])]
    else:
        anslist = anslist + [calcAdvDec(testvalues[i])]
    immlist = immlist + [calcAdvDec(testvalues[i])]
    i+=1

closedata["AdvDec"] = immlist
closedata["sumAdvDec"] = anslist


dates = closedata.index

def makegraph (lstdata, ylabel, mainTitle):
  fig, (ax0) = plt.subplots(1, 1, sharex=True, constrained_layout=True)
  # # Price:
  ax0.plot(dates, lstdata, label = ylabel)
  ax0.legend(loc='upper right')
  ax0.set_ylabel(ylabel) 
  ax0.set_title(mainTitle, loc='left')
  return ax0
closegraph = makegraph(closedata["sumAdvDec"], str("culmadvdec"), 'MMM AOS ABT Advance Decline')

print(closegraph)