#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: ./iqr.py
Options:

Example:
 ./iqr.py 
"""

import pandas as pd
import numpy as np

#parameter(inp)
param = "1012_V1R3XP_4RAW"
#########################

count = 0
with open(param+"-time-cut.csv") as f:
     for line in f:
         count += 1
seconds = int((count - 2)/100)

for i in range(0,seconds,10):  ##Isoperimetric sequence with zero first term and 10 intersections.
   inp = param + "-class-" + str(i) + "A.csv"
   df = pd.read_csv(inp)
   print(inp)
   p25_1 = df["Axis1"].quantile(0.25) #25th percentile
   p75_1 = df["Axis1"].quantile(0.75) #75th percentile
   iqr1 = p75_1 - p25_1 #IQR: Interquartile Range. difference between the 75th and 25th percentiles
   print("IQR1 is " +str(iqr1))

   p25_2 = df["Axis2"].quantile(0.25) #25th percentile
   p75_2 = df["Axis2"].quantile(0.75) #75th percentile
   iqr2 = p75_2 - p25_2 #IQR: Interquartile Range. difference between the 75th and 25th percentiles
   print("IQR2  is " +str(iqr2))

   p25_3 = df["Axis3"].quantile(0.25) #25th percentile
   p75_3 = df["Axis3"].quantile(0.75) #75th percentile
   iqr3 = p75_3 - p25_3 #IQR: Interquartile Range. difference between the 75th and 25th percentiles
   print("IQR3  is " +str(iqr3))

   p25_4 = df["Axis4"].quantile(0.25) #25th percentile
   p75_4 = df["Axis4"].quantile(0.75) #75th percentile
   iqr4 = p75_4 - p25_4 #IQR: Interquartile Range. difference between the 75th and 25th percentiles
   print("IQR4  is " +str(iqr4))

   p25_5 = df["Axis5"].quantile(0.25) #25th percentile
   p75_5 = df["Axis5"].quantile(0.75) #75th percentile
   iqr5 = p75_5 - p25_5 #IQR: Interquartile Range. difference between the 75th and 25th percentiles
   print("IQR5  is " +str(iqr5))

   p25_6 = df["Axis6"].quantile(0.25) #25th percentile
   p75_6 = df["Axis6"].quantile(0.75) #75th percentile
   iqr6 = p75_6 - p25_6 #IQR: Interquartile Range. difference between the 75th and 25th percentiles
   print("IQR6  is " +str(iqr6))

   features = [[iqr1,iqr2,iqr3,iqr4,iqr5,iqr6]]
   nd_features = np.array(features)
   with open("iqr-" + str(i) + "A.csv", "a") as f_handle:
       np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
