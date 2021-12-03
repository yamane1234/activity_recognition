#次数p=4の場合

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as dates
import numpy.linalg as LA
import datetime as dt
from pandas.plotting import register_matplotlib_converters

#parameter(inp)
param = "1012_V1R3XP_4RAW"
#########################

#データの読み込みと格納したデータの確認
count = 0
with open(param+"-time-cut.csv") as f:
      for line in f:
          count += 1
seconds = int((count - 2)/100)
#print(seconds)
 
#for i in range(0,60,10):
for i in range(0,seconds,10):  #初項0, 交差10の等差数列。secondsより小さい範囲で生成。
    inp = param + "-class-" + str(i) + "A.csv"
#inp = param + "-class" + ".csv"
    df = pd.read_csv(inp)
    header = df.columns.values.tolist()
    data = df.values
#    print(data)
#exit()

#時系列データの格納
    y1 = np.array(data[:,2]) #Axis1 (0から数えて2列目)
    y2 = np.array(data[:,3]) #Axis2 (0から数えて3列目)
    y3 = np.array(data[:,4]) #Axis3 (0から数えて4列目)
    y4 = np.array(data[:,5]) #Axis4 (0から数えて5列目)
    y5 = np.array(data[:,6]) #Axis5 (0から数えて6列目) 
    y6 = np.array(data[:,7]) #Axis6 (0から数えて7列目)

#y1 = np.array(data[:,1]) #Axis1 (0から数えて1列目)
#y2 = np.array(data[:,2]) #Axis2 (0から数えて2列目)
#y3 = np.array(data[:,3]) #Axis3 (0から数えて3列目)
#y4 = np.array(data[:,4]) #Axis4 (0から数えて4列目)
#y5 = np.array(data[:,5]) #Axis5 (0から数えて5列目) 
#y6 = np.array(data[:,6]) #Axis6 (0から数えて6列目)


#関数を定義
    def arc(d):
      y_1 = d
      y_1 = np.insert(y_1, 0, 0)
      y_1 = np.delete(y_1, y_1.shape[0]-1)

      y_2 = y_1
      y_2 = np.insert(y_2, 0, 0)
      y_2 = np.delete(y_2, y_2.shape[0]-1)

      y_3 = y_2
      y_3 = np.insert(y_3, 0, 0)
      y_3 = np.delete(y_3, y_3.shape[0]-1)

      y_4 = y_3
      y_4 = np.insert(y_4, 0, 0)
      y_4 = np.delete(y_4, y_4.shape[0]-1)

      phi_0 = np.mean(d*d)
      phi_1 = np.mean(d*y_1)
      phi_2 = np.mean(d*y_2)
      phi_3 = np.mean(d*y_3)
      phi_4 = np.mean(d*y_4)

#テプリッツ行列の作成
      Phi = np.zeros(16).reshape((4,4)) #0からなる4x4の正方行列
      phi_list = np.array([phi_0, phi_1,phi_2,phi_3])

      for i in range(4):
       Phi[i,i] = phi_list[0]

      for i in range(3):
       Phi[i, i+1] = phi_list[1]
       Phi[i+1, i] = phi_list[1]

      for i in range(2):
       Phi[i, i+2] = phi_list[2]
       Phi[i+2, i] = phi_list[2]
  
      for i in range(1):
       Phi[i, i+3] = phi_list[3]
       Phi[i+3, i] = phi_list[3]

#係数(ARC)を求める計算
      Phi_list = np.array([phi_1, phi_2, phi_3, phi_4])
      A = LA.inv(Phi) @ Phi_list.T
      return A  #戻り値を設定

#関数を実行
    print(str(i))
    print("ARC are " + str(arc(y1)))
    print("ARC are " + str(arc(y2)))
    print("ARC are " + str(arc(y3)))
    print("ARC are " + str(arc(y4)))
    print("ARC are " + str(arc(y5)))
    print("ARC are " + str(arc(y6)))

    arc1 = arc(y1)
    arc2 = arc(y2)
    arc3 = arc(y3)
    arc4 = arc(y4)
    arc5 = arc(y5)
    arc6 = arc(y6)

    features = [arc1,arc2,arc3,arc4,arc5,arc6]
    nd_features = np.array(features)
#    with open("arc_p4.csv", "a") as f_handle:
    with open("arc_p4-" + str(i) + "A.csv", "a") as f_handle:
       np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   




#予測データの可視化
#y_list = (A[0]*y_1 + A[1]*y_2 + A[2]*y_3 + A[3]*y_4)

#fig, ax = plt.subplots(figsize=(12, 8))
#ax.plot(data[:,0][4:], data[:,1][4:]) #次数pが4なので5つ目のデータから出力
#ax.plot(data[:,0][4:], y_list[4:])

#print(y_list[4:])
#np.savetxt("./arc.txt",y_list)

#ax.plot(x_list[2:], data[:,1][2:])
#ax.plot(x_list[2:], y_list[2:])
#plt.xticks(rotation=90)
#ax.xaxis.set_major_locator(dates.MonthLocator())
#ax.xaxis.set_major_formatter(dates.DateFormatter('%Y/%m'))
#plt.show()
