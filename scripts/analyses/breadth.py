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