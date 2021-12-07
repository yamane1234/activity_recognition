#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: ./arc_p4.py 
Options:

Example:
 ./arc_p4.py
"""

#in the case of p=4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as dates
import numpy.linalg as LA
import datetime as dt
from pandas.plotting import register_matplotlib_converters

#parameter
param = "1012_V1R3XP_4RAW"
#########################

#load data and check the stored data 
count = 0
with open(param+"-time-cut.csv") as f:
      for line in f:
          count += 1
seconds = int((count - 2)/100)
 
for i in range(0,seconds,10):  #Isoperimetric sequence with zero first term and 10 intersections.
    inp = param + "-class-" + str(i) + "A.csv"
    df = pd.read_csv(inp)
    header = df.columns.values.tolist()
    data = df.values

#store time-series data 
    y1 = np.array(data[:,2]) #Axis1 (second row, counting from zero)
    y2 = np.array(data[:,3]) #Axis2 (third row, counting from zero)
    y3 = np.array(data[:,4]) #Axis3 (forth row, counting from zero)
    y4 = np.array(data[:,5]) #Axis4 (fifth row, counting from zero)
    y5 = np.array(data[:,6]) #Axis5 (sixth row, counting from zero) 
    y6 = np.array(data[:,7]) #Axis6 (seventh row, counting from zero)

#define the function
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

#create a Teplitz matrix
      Phi = np.zeros(16).reshape((4,4)) #4x4 square matrix consisting of 0
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

#calculation to find the coefficient (ARC) 
      Phi_list = np.array([phi_1, phi_2, phi_3, phi_4])
      A = LA.inv(Phi) @ Phi_list.T
      return A  #set the return value 

#execute the function
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
    with open("arc_p4-" + str(i) + "A.csv", "a") as f_handle:
       np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
