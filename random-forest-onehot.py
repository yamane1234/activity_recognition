#usage: python acc.py < input.csv

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from pandas.plotting import scatter_matrix

##training data##
df = pd.read_csv('features_edited-1011-1041.csv')
#df = pd.read_csv('features_edited-select5.csv')
print(df.columns[np.isnan(df).any()]) #NaNを一つでも含む列名を表示
#df = df.drop(df.columns[np.isnan(df).any()], axis=1) #NaNを一つでも含む列を削除
#df = df.dropna() #Delete rows which have NaN.
pre = df[(df['ID']<=1010) | (df['ID']>=1012)] #処理範囲を決める
print(pre['Class'].value_counts()) 

train_x_pre = pre.drop(['Class'],axis=1) #'Class'というカラムを除く
train_x = train_x_pre.drop(['ID'],axis=1)#'ID'というカラムを除く
print(train_x)

X = np.array(pre['Class']).reshape(-1,1)
enc = OneHotEncoder(categories="auto", sparse=False,dtype=np.float32)
onehot_X = enc.fit_transform(X) #onehot encodingを行う。クラスの値による上下をなくすため。
train_y = onehot_X
print(train_y)

##test data##
pre2 = df[(df['ID']>1010) & (df['ID']<1012)] #処理範囲を決める
print(pre2['Class'].value_counts())

test_x_pre = pre2.drop(['Class'],axis=1)
test_x = test_x_pre.drop(['ID'],axis=1)
print(test_x)
 
X2 = np.array(pre2['Class']).reshape(-1,1)
enc = OneHotEncoder(categories="auto", sparse=False,dtype=np.float32)
onehot_X2 = enc.fit_transform(X2)
test_y = onehot_X2
print(test_y)

#機械学習のモデルを作成するトレーニング用と評価用の2種類に分割する
#train_x = df.drop(['Class'], axis=1) #説明変数のみにする
#train_y = onehot_X #正解クラス
#train_y = df['Class'] #正解クラス
#(train_x, test_x, train_y, test_y) = train_test_split(train_x, train_y, test_size = 0.3, random_state = 42)
#(train_x, test_x, train_y, test_y) = train_test_split(train_x, train_y, test_size = 0.2, random_state = 42)
#訓練用の説明変数と正解クラス、評価用の説明変数と正解クラスに分割

#識別モデルの構築
#random_forest = RandomForestClassifier(max_depth=30, n_estimators=30, random_state=42)
#random_forest = RandomForestClassifier(max_depth=30, n_estimators=2500, random_state=42)
random_forest = RandomForestClassifier(max_depth=19, n_estimators=37, random_state=0, criterion="entropy")
random_forest.fit(train_x, train_y)

#予測値算出
y_pred = random_forest.predict(test_x)

#モデルを作成する段階でのモデルの識別精度
trainaccuracy_random_forest = random_forest.score(train_x,train_y)
print('TrainAccuracy:{}'.format(trainaccuracy_random_forest))

#print(test_y)
print(test_y.shape)
#print(y_pred)
print(y_pred.shape)

#作成したモデルに学習に使用していない評価用のデータセットを入力し精度を確認
accuracy_random_forest = accuracy_score(test_y,y_pred)
print('Accuracy:{}'.format(accuracy_random_forest))

#confusion matrix
#mat = confusion_matrix(test_y, y_pred)
#mat = confusion_matrix(test_y.values.argmax(axis=1), y_pred.argmax(axis=1))
d = classification_report(test_y.argmax(axis=1), y_pred.argmax(axis=1), output_dict=True)
df_cla = pd.DataFrame(d)
print(df_cla)
df_cla.to_csv(r"./classification_report1.csv")

mat = confusion_matrix(test_y.argmax(axis=1), y_pred.argmax(axis=1))
sns.heatmap(mat, square=True, annot=True, cbar=False, fmt='d', cmap='RdPu')
plt.xlabel('predicted class')
plt.ylabel('true value')
#plt.show()
plt.savefig('confusion_matrix1.jpg')

#変数の重要度を可視化
importance = pd.DataFrame({'変数':train_x.columns, '重要度':random_forest.feature_importances_})
print(importance)
importance.to_csv(r"./importance1.csv") #csv fileに出力

#特徴量をプロット
#plt.scatter(df['variance1'], df['max1'], c=df['Class'])
#plt.xlabel('variance1')
#plt.ylabel('max1')
#plt.show()
#plt.savefig('features01.jpg')

