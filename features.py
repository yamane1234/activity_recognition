#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: ./features.py < input.csv
Options:

Example:
 ./features.py < input.csv
"""
##Import libraries##
from statistics import mean, stdev, variance, median
import sys
import math
import numpy as np
import pandas as pd
import scipy.stats

#Read data and make a list of each axis. 
axis = []
for line in sys.stdin.readlines():
    i = line.rstrip().split(",")
    axis.append(i)
axis.pop(0) #Delete a label in the first line. 
cla = axis[0][0] #Classification class.

axis1 = []
axis2 = []
axis3 = []
axis4 = []
axis5 = []
axis6 = []
for j in range(len(axis)):
    a = axis[j][2]
    b = axis[j][3]
    c = axis[j][4]
    d = axis[j][5]
    e = axis[j][6]
    f = axis[j][7]

   # a = axis[j][1]
   # b = axis[j][2]
   # c = axis[j][3]
   # d = axis[j][4]
   # e = axis[j][5]
   # f = axis[j][6]
    axis1.append(float(a))
    axis2.append(float(b))
    axis3.append(float(c))
    axis4.append(float(d))
    axis5.append(float(e))
    axis6.append(float(f))

#mean and sd
m1 = mean(axis1)
m2 = mean(axis2)
m3 = mean(axis3)
m4 = mean(axis4)
m5 = mean(axis5)
m6 = mean(axis6)
#print('mean axis1: {0:.2f}'.format(m1))
#print('mean axis2: {0:.2f}'.format(m2))
#print('mean axis3: {0:.2f}'.format(m3))

stdev1 = stdev(axis1)
stdev2 = stdev(axis2)
stdev3 = stdev(axis3)
stdev4 = stdev(axis4)
stdev5 = stdev(axis5)
stdev6 = stdev(axis6)
#print('stdev axis1: {0:.4f}'.format(stdev1))
#print('stdev axis2: {0:.4f}'.format(stdev2))
#print('stdev axis3: {0:.4f}'.format(stdev3))

#variance
var1 = variance(axis1)
var2 = variance(axis2)
var3 = variance(axis3)
var4 = variance(axis4)
var5 = variance(axis5)
var6 = variance(axis6)

#median
med1 = median(axis1)
med2 = median(axis2)
med3 = median(axis3)
med4 = median(axis4)
med5 = median(axis5)
med6 = median(axis6)

#cv
#cv1 = stdev1/abs(m1)
#cv2 = stdev2/abs(m2)
#cv3 = stdev3/abs(m3)
#print('cv axis1: {0:.2f}'.format(cv1))
#print('cv axis2: {0:.2f}'.format(cv2))
#print('cv axis3: {0:.2f}'.format(cv3))

#signal power
signal1 = []
signal2 = []
signal3 = []
for k in range(len(axis1)):
    s1 = axis1[k]**2
    s2 = axis2[k]**2
    s3 = axis3[k]**2
    signal1.append(s1)
    signal2.append(s2)
    signal3.append(s3)
sp1 = sum(signal1)
sp2 = sum(signal2)
sp3 = sum(signal3)
#print('signal power axis1: {0:.2f}'.format(sp1))
#print('signal power axis2: {0:.2f}'.format(sp2))
#print('signal power axis3: {0:.2f}'.format(sp3))   

##log energy## 
#log1 = []
#log2 = []
#log3 = []
#for l in range(len(axis1)):
#    lg1 = math.log(axis1[l]**2)  #Numbers smaller than the next largest floating point number after 0 are rounded to 0 by nearest rounding, resulting in a domain error.
#    lg2 = math.log(axis2[l]**2)
#    lg3 = math.log(axis3[l]**2)
#    log1.append(lg1)
#    log2.append(lg2)
#    log3.append(lg3)
#log_energy1 = sum(log1)
#log_energy2 = sum(log2)
#log_energy3 = sum(log3)
#print('log energy axis1: {0:.2f}'.format(log_energy1))
#print('log energy axis2: {0:.2f}'.format(log_energy2))
#print('log energy axis3: {0:.2f}'.format(log_energy3))

#lag one autocorrelation
deno1 = []
deno2 = []
deno3 = []
deno4 = []
deno5 = []
deno6 = []
for i in range(len(axis1)):
    diff1a = (axis1[i]-m1)**2
    diff2a = (axis2[i]-m2)**2
    diff3a = (axis3[i]-m3)**2
    diff4a = (axis4[i]-m4)**2
    diff5a = (axis5[i]-m5)**2
    diff6a = (axis6[i]-m6)**2
    deno1.append(diff1a)
    deno2.append(diff2a)
    deno3.append(diff3a)
    deno4.append(diff4a)
    deno5.append(diff5a)
    deno6.append(diff6a)
dn1 = sum(deno1)
dn2 = sum(deno2)
dn3 = sum(deno3)
dn4 = sum(deno4)
dn5 = sum(deno5)
dn6 = sum(deno6)

#If dn == 0, end the process as error to avoid deviding by dn. 
if dn1 == 0:
   print("dn1 = 0, error")
   features = [["dn1 = 0, error"]]
   nd_features = np.array(features)
   with open("features.csv", "a") as f_handle:
       np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   exit()

elif dn2 == 0: 
   print("dn2 = 0, error") 
   features = [["dn2 = 0, error"]] 
   nd_features = np.array(features)
   with open("features.csv", "a") as f_handle:      
        np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   exit()

elif dn3 == 0:
   print("dn3 = 0, error") 
   features = [["dn3 = 0, error"]] 
   nd_features = np.array(features)
   with open("features.csv", "a") as f_handle:      
        np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   exit()

elif dn4 == 0:
   print("dn4 = 0, error") 
   features = [["dn4 = 0, error"]] 
   nd_features = np.array(features)
   with open("features.csv", "a") as f_handle:      
        np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   exit()

elif dn5 == 0:
   print("dn5 = 0, error") 
   features = [["dn5 = 0, error"]] 
   nd_features = np.array(features)
   with open("features.csv", "a") as f_handle:      
        np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   exit()

elif dn6 == 0:
   print("dn6 = 0, error") 
   features = [["dn6 = 0, error"]] 
   nd_features = np.array(features)
   with open("features.csv", "a") as f_handle:      
        np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")
   exit()

nume1 = []
nume2 = []
nume3 = []
for i in range(len(axis1)-1):
    diff1b = (axis1[i]-m1)
    diff1c = (axis1[i+1]-m1)
    multi1 = diff1b * diff1c
    diff2b = (axis2[i]-m2)
    diff2c = (axis2[i+1]-m2)
    multi2 = diff2b * diff2c    
    diff3b = (axis3[i]-m3)
    diff3c = (axis3[i+1]-m3)
    multi3 = diff3b * diff3c
    nume1.append(multi1)
    nume2.append(multi2)
    nume3.append(multi3)
nm1 = sum(nume1)
nm2 = sum(nume2)
nm3 = sum(nume3)

#auto1 = nm1/dn1
#auto2 = nm2/dn2
#auto3 = nm3/dn3

#print('lag one autocorrelation axis1: {0:.2f}'.format(auto1))
#print('lag one autocorrelation axis2: {0:.2f}'.format(auto2))
#print('lag one autocorrelation axis3: {0:.2f}'.format(auto3))

#Kurtosis
dn_ku1 = (dn1/len(axis1))**3
dn_ku2 = (dn2/len(axis2))**3
dn_ku3 = (dn3/len(axis3))**3
dn_ku4 = (dn4/len(axis4))**3
dn_ku5 = (dn5/len(axis5))**3
dn_ku6 = (dn6/len(axis6))**3

nume_ku1 = []
nume_ku2 = []
nume_ku3 = []
nume_ku4 = []
nume_ku5 = []
nume_ku6 = []
for i in range(len(axis1)):
     diff1d = (axis1[i]-m1)**4
     diff2d = (axis2[i]-m2)**4
     diff3d= (axis3[i]-m3)**4
     diff4d= (axis4[i]-m4)**4
     diff5d= (axis5[i]-m5)**4
     diff6d= (axis6[i]-m6)**4
     nume_ku1.append(diff1d)
     nume_ku2.append(diff2d)
     nume_ku3.append(diff3d)
     nume_ku4.append(diff4d)
     nume_ku5.append(diff5d)
     nume_ku6.append(diff6d)
nm_ku1 = sum(nume_ku1)/len(axis1)
nm_ku2 = sum(nume_ku2)/len(axis2)
nm_ku3 = sum(nume_ku3)/len(axis3)
nm_ku4 = sum(nume_ku4)/len(axis4)
nm_ku5 = sum(nume_ku5)/len(axis5)
nm_ku6 = sum(nume_ku6)/len(axis6)

kurtosis1 = nm_ku1/dn_ku1-3
kurtosis2 = nm_ku2/dn_ku2-3
kurtosis3 = nm_ku3/dn_ku3-3 
kurtosis4 = nm_ku4/dn_ku4-3 
kurtosis5 = nm_ku5/dn_ku5-3 
kurtosis6 = nm_ku6/dn_ku6-3 

#print('kurtosis axis1: {0:.2f}'.format(kurtosis1))
#print('kurtosis axis2: {0:.2f}'.format(kurtosis2))
#print('kurtosis axis3: {0:.2f}'.format(kurtosis3))

#Skewness
dn_sk1 = (dn1/len(axis1))**(3/2)
dn_sk2 = (dn2/len(axis2))**(3/2)
dn_sk3 = (dn3/len(axis3))**(3/2)
dn_sk4 = (dn4/len(axis4))**(3/2)
dn_sk5 = (dn5/len(axis5))**(3/2)
dn_sk6 = (dn6/len(axis6))**(3/2)

nume_sk1 = []
nume_sk2 = []
nume_sk3 = []
nume_sk4 = []
nume_sk5 = []
nume_sk6 = []
for i in range(len(axis1)):
     diff1e = (axis1[i]-m1)**3
     diff2e = (axis2[i]-m2)**3
     diff3e= (axis3[i]-m3)**3
     diff4e= (axis4[i]-m4)**3
     diff5e= (axis5[i]-m5)**3
     diff6e= (axis6[i]-m6)**3
     nume_sk1.append(diff1e)
     nume_sk2.append(diff2e)
     nume_sk3.append(diff3e)
     nume_sk4.append(diff4e)
     nume_sk5.append(diff5e)
     nume_sk6.append(diff6e)
nm_sk1 = sum(nume_sk1)/len(axis1)
nm_sk2 = sum(nume_sk2)/len(axis2)
nm_sk3 = sum(nume_sk3)/len(axis3)
nm_sk4 = sum(nume_sk4)/len(axis4)
nm_sk5 = sum(nume_sk5)/len(axis5)
nm_sk6 = sum(nume_sk6)/len(axis6)

skewness1 = nm_sk1/dn_sk1
skewness2 = nm_sk2/dn_sk2
skewness3 = nm_sk3/dn_sk3
skewness4 = nm_sk4/dn_sk4
skewness5 = nm_sk5/dn_sk5
skewness6 = nm_sk6/dn_sk6

#print('skewness axis1: {0:.2f}'.format(skewness1))
#print('skewness axis2: {0:.2f}'.format(skewness2))
#print('skewness axis3: {0:.2f}'.format(skewness3))

#root mean square
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
for k in range(len(axis1)):
     s1 = axis1[k]**2
     s2 = axis2[k]**2
     s3 = axis3[k]**2
     s4 = axis4[k]**2
     s5 = axis5[k]**2
     s6 = axis6[k]**2
     r1.append(s1)
     r2.append(s2)
     r3.append(s3)
     r4.append(s4)
     r5.append(s5)
     r6.append(s6)
rms1 = np.sqrt(mean(r1))
rms2 = np.sqrt(mean(r2))
rms3 = np.sqrt(mean(r3))
rms4 = np.sqrt(mean(r4))
rms5 = np.sqrt(mean(r5))
rms6 = np.sqrt(mean(r6))

#max
max1 = max(axis1)
max2 = max(axis2)
max3 = max(axis3)
max4 = max(axis4)
max5 = max(axis5)
max6 = max(axis6)

#min
min1 = min(axis1)
min2 = min(axis2)
min3 = min(axis3)
min4 = min(axis4)
min5 = min(axis5)
min6 = min(axis6)

#max - min difference
diff1 = max(axis1) - min(axis1)
diff2 = max(axis2) - min(axis2)
diff3 = max(axis3) - min(axis3)

#mean absolute deviation (mad)
series1 = pd.Series(axis1)
series2 = pd.Series(axis2)
series3 = pd.Series(axis3)
mad1 = series1.mad()
mad2 = series2.mad()
mad3 = series3.mad()

#signal magnitude area (SMA)
SMA = []
for k in range(len(axis1)):
      m1 = abs(axis1[k]) #Calculate the absolute value.
      m2 = abs(axis2[k])
      m3 = abs(axis3[k])
      s = m1+m2+m3
      SMA.append(s)
sma_hip = mean(SMA)    

SMA2 = []
for k in range(len(axis4)):
      m4 = abs(axis4[k])
      m5 = abs(axis5[k])
      m6 = abs(axis6[k])
      s = m4 + m5 + m6
      SMA2.append(s)
sma_wrist = mean(SMA2)

#pairwise correlation between the axes (Hip) 
#denominator
deno1 = []
deno2 = []
deno3 = []
for i in range(len(axis1)):
     diff1a = (axis1[i]-m1)**2
     diff2a = (axis2[i]-m2)**2
     diff3a = (axis3[i]-m3)**2
     deno1.append(diff1a)
     deno2.append(diff2a)
     deno3.append(diff3a)
dn1 = sum(deno1)
dn2 = sum(deno2)
dn3 = sum(deno3)
dn13 = math.sqrt(dn1 * dn3)
dn12 = math.sqrt(dn1 * dn2)
dn23 = math.sqrt(dn2 * dn3)
#numerator
nume13 = []
nume12 = []
nume23 = []
for i in range(len(axis1)):
     diff1b = (axis1[i]-m1)
     diff2b = (axis2[i]-m2)
     diff3b = (axis3[i]-m3)
     multi13 = diff1b * diff3b
     multi12 = diff1b * diff2b
     multi23 = diff2b * diff3b
     nume13.append(multi13)
     nume12.append(multi12)
     nume23.append(multi23)
nm13 = sum(nume13)
nm12 = sum(nume12)
nm23 = sum(nume23)
#correlation
corr13 = nm13/dn13 #xz
corr12 = nm12/dn12 #xy
corr23 = nm23/dn23 #yz

#pairwise correlation between the axes (Wrist) 
#denominator
deno4 = []
deno5 = []
deno6 = []
for i in range(len(axis1)):
      diff4a = (axis4[i]-m4)**2
      diff5a = (axis5[i]-m5)**2
      diff6a = (axis6[i]-m6)**2
      deno4.append(diff4a)
      deno5.append(diff5a)
      deno6.append(diff6a)
dn4 = sum(deno4)
dn5 = sum(deno5)
dn6 = sum(deno6)
dn46 = math.sqrt(dn4 * dn6)
dn45 = math.sqrt(dn4 * dn5)
dn56 = math.sqrt(dn5 * dn6)
#numerator
nume46 = []
nume45 = []
nume56 = []
for i in range(len(axis4)):
      diff4b = (axis4[i]-m4)
      diff5b = (axis5[i]-m5)
      diff6b = (axis6[i]-m6)
      multi46 = diff4b * diff6b
      multi45 = diff4b * diff5b
      multi56 = diff5b * diff6b
      nume46.append(multi46)
      nume45.append(multi45)
      nume56.append(multi56)
nm46 = sum(nume46)
nm45 = sum(nume45)
nm56 = sum(nume56)
#correlation
corr46 = nm46/dn46 #xz
corr45 = nm45/dn45 #xy
corr56 = nm56/dn56 #yz



#Frequency domain entropy (Power Spectral Entropy) and Energy
def entropy(data):
   N = len(data) #number of data
   axis_arr = np.array(data) #Convert list to numpy array. 
   F = np.fft.fft(axis_arr) #FFT
   F_abs = np.abs(F) #Convert complex number to absolute value.
   F_abs_amp = F_abs/N * 2 #Divide alternating current by the number of data and double it.
   PSD = (F_abs_amp **2)/N #Calculate the PSD of your signal by simply squaring the amplitude spectrum and scaling it by number of frequency bins.
   PSD_N = PSD/sum(PSD) #Normalize the calculated PSD by dividing it by a total sum. 
   eng = sum(F_abs_amp **2)/N #Energy
   ent = 0
   for i in range(N):
       if PSD_N[i] == 0:
             print("PSD_N = 0")
             continue           #If PSD_N=0, do not calculate log2 (antilogarithm > 0).
       ent += PSD_N[i]*np.log2(PSD_N[i]) #Calculate the Power Spectral Entropy using a standard formula for entropy calculation.
   return -ent, eng

results1 = entropy(axis1) #Execute the function to calculate entropy and energy. 
results2 = entropy(axis2)
results3 = entropy(axis3)
results4 = entropy(axis4)
results5 = entropy(axis5)
results6 = entropy(axis6)

H1 = results1[0]
E1 = results1[1]
H2 = results2[0]
E2 = results2[1]
H3 = results3[0]
E3 = results3[1]
H4 = results4[0]
E4 = results4[1]
H5 = results5[0]
E5 = results5[1]
H6 = results6[0]
E6 = results6[1]

#csv output
#features = [["class","mean1","mean2","mean3","stdev1","stdev2","stdev3","cv1","cv2","cv3","lag one autocorrelation1","lag one autocorrelation2","lag one autocorrelation3","skewness1","skewness2","skewness3","kurtosis1","kurtosis2","kurtosis3","signal power1","signal power2","signal power3","log energy1","log energy2","log energy3"],[cla,m1,m2,m3,stdev1,stdev2,stdev3,cv1,cv2,cv3,auto1,auto2,auto3,skewness1,skewness2,skewness3,kurtosis1,kurtosis2,kurtosis3,sp1,sp2,sp3,log_energy1,log_energy2,log_energy3]]
#nd_features = np.array(features)
#np.savetxt("features.csv", nd_features, delimiter=",", fmt="%s")

#csv output
#features = [[cla,m1,m2,m3,stdev1,stdev2,stdev3,cv1,cv2,cv3,auto1,auto2,auto3,skewness1,skewness2,skewness3,kurtosis1,kurtosis2,kurtosis3,sp1,sp2,sp3,log_energy1,log_energy2,log_energy3]]
#features = [[cla,m1,m2,m3,stdev1,stdev2,stdev3,cv1,cv2,cv3,auto1,auto2,auto3,skewness1,skewness2,skewness3,kurtosis1,kurtosis2,kurtosis3,sp1,sp2,sp3,rms1,rms2,rms3,diff1,diff2,diff3,mad1,mad2,mad3,sma,corr13,corr12,corr23,H1,H2,H3,E1,E2,E3]]
 
features = [[cla,m1,m2,m3,m4,m5,m6,stdev1,stdev2,stdev3,stdev4,stdev5,stdev6,var1,var2,var3,var4,var5,var6,max1,max2,max3,max4,max5,max6,min1,min2,min3,min4,min5,min6,rms1,rms2,rms3,rms4,rms5,rms6,sma_hip,sma_wrist,corr13,corr12,corr23,corr46,corr45,corr56,H1,H2,H3,H4,H5,H6,E1,E2,E3,E4,E5,E6,kurtosis1,kurtosis2,kurtosis3,kurtosis4,kurtosis5,kurtosis6,skewness1,skewness2,skewness3,skewness4,skewness5,skewness6,med1,med2,med3,med4,med5,med6]]
nd_features = np.array(features)
with open("features.csv", "a") as f_handle:
     np.savetxt(f_handle, nd_features, delimiter=",", fmt="%s")

