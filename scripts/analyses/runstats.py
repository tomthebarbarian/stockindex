# TODO Create analyses with numpy etc

import importlib.util
import sys,os
import yfinance as yf
from importlib.machinery import SourceFileLoader
spec = importlib.util.spec_from_file_location("inxlst", "scripts/imports/indexlist.py")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

highlowdata = pd.read_csv("first3highlow.csv")
print(highlowdatas)