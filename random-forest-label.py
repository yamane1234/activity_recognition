#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: ./random-forest-label.py 
Options:

Example:
 ./random-forest-label.py
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from itertools import cycle
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from seaborn_analyzer import classplot
from pandas.plotting import scatter_matrix
from PIL import Image


##training data##
df = pd.read_csv('features_edited-1011-1041.csv')
pre = df[(df['ID']<=1010) | (df['ID']>=1012)] #processing range
print(pre['Class'].value_counts()) 
train_x_pre = pre.drop(['Class'],axis=1) #remove 'Class' column 
train_x = train_x_pre.drop(['ID'],axis=1)#remove 'ID' column 
print(train_x)
train_y = np.array(pre['Class']) 

##test data##
pre2 = df[(df['ID']>1010) & (df['ID']<1012)] #processing range 
print(pre2['Class'].value_counts())
test_x_pre = pre2.drop(['Class'],axis=1)
test_x = test_x_pre.drop(['ID'],axis=1)
print(test_x)
test_y = np.array(pre2['Class']) 
print(test_y)

#Build an identification model
random_forest = RandomForestClassifier(max_depth=30, n_estimators=2500, random_state=42)
random_forest.fit(train_x, train_y)

#Calculation of predicted value
y_pred = random_forest.predict(test_x)

#Identification accuracy of the model at the stage of creating the model
trainaccuracy_random_forest = random_forest.score(train_x,train_y)
print('TrainAccuracy:{}'.format(trainaccuracy_random_forest))

#Input an evaluation dataset that is not used for training into the created model to check the accuracy.
accuracy_random_forest = accuracy_score(test_y,y_pred)
print('Accuracy:{}'.format(accuracy_random_forest))

#Confusion matrix
d = classification_report(test_y.argmax(axis=1), y_pred.argmax(axis=1), output_dict=True)
df_cla = pd.DataFrame(d)
print(df_cla)
df_cla.to_csv(r"./classification_report1.csv")

mat = confusion_matrix(test_y.argmax(axis=1), y_pred.argmax(axis=1))
sns.heatmap(mat, square=True, annot=True, cbar=False, fmt='d', cmap='RdPu')
plt.xlabel('predicted class')
plt.ylabel('true value')

# I want to create a jpg image by matplotlib but it's difficult due to this bug.
# https://bugs.launchpad.net/ubuntu/+source/matplotlib/+bug/1897283
# A reference website is below.
# https://zenn.dev/satoru_takeuchi/articles/c4993fda858411
plt.savefig("test.png")
Image.open("test.png").convert("RGB").save("confusion_matrix1.jpg")
os.remove("test.png")

#Importance of variables.
importance = pd.DataFrame({'variables':train_x.columns, 'importance':random_forest.feature_importances_})
print(importance)
importance.to_csv(r"./importance1.csv") #output to a csv file


