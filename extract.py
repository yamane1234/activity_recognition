#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: ./extract.py
Options:

Example:
 ./extract.py
"""

##import libraries##
import numpy as np
import pandas as pd
from datetime import datetime
import pandas.tseries.offsets as offsets
import csv

##parameters(inp,inp3)##
inp="1012_V1R3XP_4RAW"
inp3 = 'file =="1012_V1R3XP_4"'
##############################

#classification class
cla=1
start="start1"
stop="stop1"
cla_txt="class.txt"
inp2="Time_Input_GT3X_Plus_Hip.csv"

#count the number of lines in inp
count = 0
with open(inp+"-time.csv") as f:
    h = next(csv.reader(f)) #skip the first line (header)
    for line in f:
        count += 1
z = count

#create class.txt
test = []
for i in range(int(z)):
    test.append(cla)
arr_test = np.array(test)
np.savetxt(cla_txt,arr_test,delimiter=",")
 
#insert the string "Class" in the first line.
with open(cla_txt) as f:
    data = f.readlines()

data.insert(0,"Class\n")
 
with open(cla_txt, mode="w") as f:
    f.writelines(data)

#add classification
df1 = pd.read_csv(cla_txt)
df2 = pd.read_csv(inp+"-time.csv")
df_concat = pd.concat([df1,df2],axis=1)
df_concat.to_csv(inp+"-time-class-combined.csv",index=None)

##extract##
df_acc = pd.read_csv(inp+"-time-class-combined.csv")
df_acc["Time"] = pd.to_datetime(df_acc["Time"]) #convert to time format
df_time = pd.read_csv(inp2)
row = df_time.reset_index().query(inp3).index[0] #get the row number from the column element

df_time["X"] = pd.to_datetime(df_time[start]) #Convert to time format and add a new column "X" to the data frame
df_time["Y"] = pd.to_datetime(df_time[stop])  #Convert to time format and add a new column "Y" to the data frame

y_X = df_time["X"][row].year
mo_X = df_time["X"][row].month
d_X = df_time["X"][row].day
h_X = df_time["X"][row].hour
mi_X = df_time["X"][row].minute
s_X = df_time["X"][row].second

y_Y = df_time["Y"][row].year
mo_Y = df_time["Y"][row].month
d_Y = df_time["Y"][row].day
h_Y = df_time["Y"][row].hour
mi_Y = df_time["Y"][row].minute
s_Y = df_time["Y"][row].second

df_acc[(df_acc["Time"] >= datetime(y_X,mo_X,d_X,h_X,mi_X,s_X)) & (df_acc["Time"] <= datetime(y_Y,mo_Y,d_Y,h_Y,mi_Y,s_Y))].to_csv(inp+"-time-cut.csv")

#cut out every 10 seconds 
df_acc = pd.read_csv(inp+"-time-cut.csv")
df_acc["Time"] = pd.to_datetime(df_acc["Time"]) #convert to time format 

df_time_add = df_time["X"][row] + offsets.Minute(0) + offsets.Second(0) #add 0min0sec

count = 0
with open(inp+"-time-cut.csv") as f:
    for line in f: 
        count += 1
seconds = int((count - 2)/100) 
print(seconds)

for i in range(0,seconds,10):  #Isoperimetric sequence with zero first term and 10 intersections
    df_time_seg1  = df_time_add + offsets.Second(i)
    df_time_seg2  = df_time_add + offsets.Second(i+10) 
    y_X = df_time_seg1.year
    mo_X = df_time_seg1.month
    d_X = df_time_seg1.day
    h_X = df_time_seg1.hour
    mi_X = df_time_seg1.minute
    s_X = df_time_seg1.second
 
    y_Y = df_time_seg2.year
    mo_Y = df_time_seg2.month
    d_Y = df_time_seg2.day
    h_Y = df_time_seg2.hour
    mi_Y = df_time_seg2.minute
    s_Y = df_time_seg2.second
 
    name = inp + "-time-cut-class-" + str(i) + ".csv"
    df_acc[(df_acc["Time"] >= datetime(y_X,mo_X,d_X,h_X,mi_ ,s_X)) & (df_acc["Time"] < datetime(y_Y,mo_Y,d_Y,h_Y,mi_Y,s_Y))].to_csv(name)
