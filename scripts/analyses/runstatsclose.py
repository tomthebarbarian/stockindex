# TODO Create analyses with numpy etc

import importlib.util
import sys,os
import yfinance as yf
from importlib.machinery import SourceFileLoader
spec = importlib.util.spec_from_file_location("inxlst", "scripts/imports/indexlist.py")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ["MMM",
#          'AOS',
#          'ABT',]

closedata = pd.read_csv("first3close.csv")
closedata = closedata.set_index("Date")
# closedata.set_index("DATE")
testvalues = closedata.index
testvalue = closedata.at["2018-01-02", "AOShigh"]
closedata["AOS"] = list(map(lambda x: 1 if (closedata.at[x, "AOShigh"] - closedata.at[x, "AOSlow"]) > 0 else -1, closedata.index))

print(closedata)

# The Formula for Advance/Decline (A/D) Line Is:
# A/D = Net Advances  +  { PA, if PA value exists else 0
# where:
# Net Advances == Difference between number of daily ascending and declining stocks 
#  PA == Previous Advances == Prior indicator reading
# ​
