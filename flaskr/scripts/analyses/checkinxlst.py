# from ..imports.indexlist import spinx as ticksym
# print(ticksym)
import os
import sys
import pandas as pd


script_dir = os.path.dirname( __file__ )
# Moves to the main stock inx file
# is it uneccessary if I run a super main?
mymodule_dir = os.path.join( script_dir, '..', '..', 'data')
sys.path.append( mymodule_dir )


spdata = pd.read_csv("data/SPTickerWiki.csv")
ticksym = spdata['Symbol']


print(ticksym[0])
print(ticksym[1])

