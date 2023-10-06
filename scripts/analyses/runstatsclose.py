# TODO Create analyses with numpy etc
import sys,os
# from .scripts.imports import spinx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', '..', 'data')
sys.path.append( mymodule_dir )


spdata = pd.read_csv("data/SPTickerWiki.csv")
ticksymlst = spdata['Symbol']

closedata = pd.read_csv("results/500close.csv")


# calcAdvDec calculates Advance and decline for inx (a data frameindex) and ticksym (stock ticker symbol)
# returns if the stock advanced, declined or remained the same that day
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


closedata = closedata.set_index("Date")


subsetdata = closedata
# subsetdata = closedata.loc['2023-01-03':'2023-04-03']

testvalues = subsetdata.index
graphdata = subsetdata


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

graphdata["AdvDec"] = immlist
graphdata["sumAdvDec"] = anslist


dates = graphdata.index

def makegraph (lstdata, ylabel, mainTitle):
  fig, (ax0) = plt.subplots(1, 1, sharex=True, constrained_layout=True)
  # # Price:
  ax0.plot(dates, lstdata, label = ylabel)
  ax0.set_xticks(ax0.get_xticks()[::20])
  ax0.legend(loc='upper right')
  ax0.set_ylabel(ylabel) 
  ax0.set_title(mainTitle, loc='left')
  return fig

closegraph = makegraph(graphdata["sumAdvDec"], str("culmadvdec"), 'SP500 Advance Decline')

# print(closegraph)
closegraph.show()
plt.savefig('results/graphs/advdecplt2019.png')