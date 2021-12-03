#!/usr/bin/env python

##usage##
##python3.7 extract.py ##

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

#分類クラス
cla=1
start="start1"
stop="stop1"
cla_txt="class.txt"
inp2="Time_Input_GT3X_Plus_Hip.csv"

#inpの行数を数える
count = 0
with open(inp+"-time.csv") as f:
    h = next(csv.reader(f)) #skip the first line (header)
    for line in f:
        count += 1
z = count

#class.txtを作成
test = []
for i in range(int(z)):
    test.append(cla)
arr_test = np.array(test)
np.savetxt(cla_txt,arr_test,delimiter=",")
 
#1行目に"Class"という文字列を挿入
with open(cla_txt) as f:
    data = f.readlines()

data.insert(0,"Class\n")
 
with open(cla_txt, mode="w") as f:
    f.writelines(data)

#分類を追加
df1 = pd.read_csv(cla_txt)
df2 = pd.read_csv(inp+"-time.csv")
df_concat = pd.concat([df1,df2],axis=1)
df_concat.to_csv(inp+"-time-class-combined.csv",index=None)


##抽出##
df_acc = pd.read_csv(inp+"-time-class-combined.csv")
df_acc["Time"] = pd.to_datetime(df_acc["Time"]) #時間形式に変換
df_time = pd.read_csv(inp2)
row = df_time.reset_index().query(inp3).index[0] #列の要素から行番号を取得

df_time["X"] = pd.to_datetime(df_time[start]) #時間形式に変換して新しい列"X"をdata frameに追加
df_time["Y"] = pd.to_datetime(df_time[stop])  #時間形式に変換して新しい列"Y"をdata frameに追加

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
#exit()

#さらに0-1 minutes を切り出す
#df_acc = pd.read_csv(inp+"-time-cut.csv")
#df_acc["Time"] = pd.to_datetime(df_acc["Time"]) #時間形式に変換
#df_time_add1 = df_time["X"][row] + offsets.Minute(0) + offsets.Second(0)
#df_time_add2 = df_time["X"][row] + offsets.Minute(1) + offsets.Second(0)

#y_X = df_time_add1.year
#mo_X = df_time_add1.month
#d_X = df_time_add1.day
#h_X = df_time_add1.hour
#mi_X = df_time_add1.minute
#s_X = df_time_add1.second
 
#y_Y = df_time_add2.year
#mo_Y = df_time_add2.month
#d_Y = df_time_add2.day
#h_Y = df_time_add2.hour
#mi_Y = df_time_add2.minute
#s_Y = df_time_add2.second

#df_acc[(df_acc["Time"] >= datetime(y_X,mo_X,d_X,h_X,mi_X,s_X)) & (df_acc["Time"] <= datetime(y_Y,mo_Y,d_Y,h_Y,mi_Y,s_Y))].to_csv(inp+"-time-cut2.csv")

#さらに10秒ごとに切り出す
#df_acc = pd.read_csv(inp+"-time-cut2.csv")
df_acc = pd.read_csv(inp+"-time-cut.csv")
df_acc["Time"] = pd.to_datetime(df_acc["Time"]) #時間形式に変換

df_time_add = df_time["X"][row] + offsets.Minute(0) + offsets.Second(0) #add 0min0sec

count = 0
with open(inp+"-time-cut.csv") as f:
    for line in f: 
        count += 1
seconds = int((count - 2)/100) 
print(seconds)

#for i in range(0,60,10):
for i in range(0,seconds,10):  #初項0, 交差10の等差数列。secondsより小さい範囲で生成。
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
    df_acc[(df_acc["Time"] >= datetime(y_X,mo_X,d_X,h_X,mi_X,s_X)) & (df_acc["Time"] < datetime(y_Y,mo_Y,d_Y,h_Y,mi_Y,s_Y))].to_csv(name)
