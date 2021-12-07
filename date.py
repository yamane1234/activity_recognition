#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: ./date.py
Options:

Example:
 ./date.py
"""

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
df = pd.date_range(start=st, end=ed, freq=(fr)) 
print(df)

df_acc["Time"] = pd.Series(df)
df_acc = df_acc[["Time","Axis1","Axis2","Axis3"]]
print(df_acc)

#output as csv
df_acc.to_csv(inp+"-time.csv")
