# from ..imports.indexlist import spinx as ticksym
# print(ticksym)
import os
import sys


script_dir = os.path.dirname( __file__ )
# Moves to the main stock inx file
# is it uneccessary if I run a super main?
mymodule_dir = os.path.join( script_dir, '..', '..', 'data')
sys.path.append( mymodule_dir )

from indexlist import spinx as ticksym
print(ticksym)

