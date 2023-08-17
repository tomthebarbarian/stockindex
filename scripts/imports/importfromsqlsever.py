from sqlalchemy import create_engine
import psycopg2
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

alchemyEngine   = create_engine('postgresql+psycopg2://tomzhang:admin@127.0.0.1:5432/stockindex', pool_recycle=3600)
# alchemyEngine   = create_engine('postgresql+psycopg2://test:@127.0.0.1:5432/stockindex', pool_recycle=3600)

dbConnection    = alchemyEngine.connect()

dataFrame       = pd.read_sql("select * from \"spclose\"", dbConnection)

pd.set_option('display.expand_frame_repr', False)

closeData = pd.read_csv("results/500close.csv")
# closeData = closeData.set_index("Date")

# Print the DataFrame

# print(closeData.index.unique().tolist()[0])
# print(list(map(lambda x: x.strftime('%Y-%m-%d'),dataFrame["Date"].unique().tolist()))[0])
# toStrTime = lambda x: x.strftime('%Y-%m-%d')

newdates = np.setdiff1d(closeData["Date"].unique().tolist(), list(map(lambda x: x.strftime('%Y-%m-%d'),dataFrame["Date"].unique().tolist())))
# newdates = np.setdiff1d(closeData["Date"].unique().tolist(), dataFrame["Date"].unique().tolist())
newRows = closeData[(closeData["Date"].isin(newdates))]

# print(newdates)
newRows.to_sql('spclose', con =dbConnection, if_exists='append', index=False)


# Close the database connection

dbConnection.close()