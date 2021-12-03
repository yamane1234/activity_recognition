import pandas as pd
import csv

#parameter(inp)
inp = "1012_V1R3XP_4RAW"
inp2 = "start-download.txt"
#########################

#count the number of lines
count = 0
with open(inp+"-edited.csv") as f:
     h = next(csv.reader(f)) #skip the first line (header)
     for line in f:
         count += 1
z = count

#read acceleration data
df_acc = pd.read_csv(inp+"-edited.csv")

#read start and downlaod time data
a = []
with open(inp2) as f:
     reader = csv.reader(f)
     for row in reader:
         a.append(row)
begin = ''.join(a[0])    #convert list into str
download = ''.join(a[1]) #convert list into str

#make time data
df = pd.date_range(start=begin, end=download, freq=('10ms')) #1行1/100s=10msが現在のActiGraphの最小単位。
#df = pd.date_range(start='15:45:00', end='16:57:55', freq=('33.3333ms'))

#add a new column (Time)
#df_acc["Time"] = pd.Series(df[(df <= df[z])]) #Convert the list/array to a pandas Series, and then when you do assignment, missing index in the Series will be filled with NaN. df <= df[z] specifies the range.
df_acc["Time"] = pd.Series(df[(df <= df[z-1])]) #Convert the list/array to a pandas Series, and then when you do assignment, missing index in the Series will be filled with NaN. df <= df[z] specifies the range.
df_acc = df_acc[["Time","Axis1","Axis2","Axis3","Axis4","Axis5","Axis6"]] #change the order
#df_acc = df_acc[["Time","Axis1","Axis2","Axis3"]] #change the order

#output as csv
df_acc.to_csv(inp+"-time.csv")
