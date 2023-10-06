# TODO Create analyses with numpy etc

import pandas as pd

highlowdata = pd.read_csv("first3highlow.csv")
highlowdata = highlowdata.set_index("Date")
# highlowdata.set_index("DATE")
testvalues = highlowdata.index
testvalue = highlowdata.at["2018-01-02", "AOShigh"]
highlowdata["AOS"] = list(map(lambda x: 1 if (highlowdata.at[x, "AOShigh"] - highlowdata.at[x, "AOSlow"]) > 0 else -1, highlowdata.index))

print(highlowdata)

# The Formula for Advance/Decline (A/D) Line Is:
# A/D = Net Advances  +  { PA, if PA value exists else 0
# where:
# Net Advances == Difference between number of daily ascending and declining stocks 
#  PA == Previous Advances == Prior indicator reading
# ​
