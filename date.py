import pandas as pd
from datetime import datetime, timedelta
import csv
 
#parameters
inp = "MOS2E04200322RAW"
st = "2020/7/30 15:57:00"
ed = "2020/8/06 13:17:32.990"
fr = '10ms'

#########################

#read acceleration data
df_acc = pd.read_csv(inp+".csv")

#dt = datetime(year=2020,month=6,day=10,hour=15,minute=6)
#dt2 = dt + timedelta(seconds=0.01)
#print(dt)
#print(dt2)

#df = pd.date_range(start="2020/6/10 14:14:00", end="2020/6/12 13:49:49", freq=('10ms')) 
df = pd.date_range(start=st, end=ed, freq=(fr)) 
print(df)

df_acc["Time"] = pd.Series(df)
df_acc = df_acc[["Time","Axis1","Axis2","Axis3"]]
print(df_acc)

#output as csv
df_acc.to_csv(inp+"-time.csv")
