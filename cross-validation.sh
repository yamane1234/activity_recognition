#!/bin/sh

###parameters###
k=31 #k-fold cross vaidation
start1=1010    #initial value
start2=1012  #initial value

value2=1011 #second value
value3=1013 #second value
add=1       #difference 
################
value1=1
value4=`echo $(($value3-1))`
value5=`echo $(($value3+$add))`
mat1=2
mat2=3

python random-forest-onehot.py
sed -e "s/<=$start1/<=$value2/g" random-forest-onehot.py | sed -e "s/>=$start2/>=$value3/g" | sed -e "s/>$start1/>$value2/g" | sed -e "s/<$start2/<$value3/g" | sed -e "s/confusion_matrix1.jpg/confusion_matrix2.jpg/g" | sed -e "s/importance1.csv/importance2.csv/g" | sed -e "s/classification_report1.csv/classification_report2.csv/g" > random-forest-onehot-new.py
mv random-forest-onehot-new.py random-forest-onehot.py

##roop##
while [ $value1 -lt $k ]  #value1がkより小さい間
do
echo $value2
echo $value3
echo $mat1
echo $mat2
python random-forest-onehot.py
sed -e "s/<=$value2/<=$value4/g" random-forest-onehot.py | sed -e "s/>=$value3/>=$value5/g" | sed -e "s/>$value2/>$value4/g" | sed -e "s/<$value3/<$value5/g" | sed -e "s/confusion_matrix${mat1}.jpg/confusion_matrix${mat2}.jpg/g" | sed -e "s/importance${mat1}.csv/importance${mat2}.csv/g" | sed -e "s/classification_report${mat1}.csv/classification_report${mat2}.csv/g" > random-forest-onehot-new.py
#sed -e "s/pre = df[(df['ID']<=$value2) | (df['ID']>=$value3)]/pre = df[(df['ID']<=$value4) | (df['ID']>=$value5)]/g" random-forest-onehot.py | sed -e "s/pre2 = df[(df['ID']>$value2) & (df['ID']<$value3)]/pre2 = df[(df['ID']>$value4) & (df['ID']<$value5)]/g" > random-forest-onehot-new.py
mv random-forest-onehot-new.py random-forest-onehot.py  
value1=`echo $(($value1+1))`
value2=`echo $(($value2+$add))`
value3=`echo $(($value3+$add))`
value4=`echo $(($value4+$add))`
value5=`echo $(($value5+$add))`
mat1=`echo $(($mat1+1))`
mat2=`echo $(($mat2+1))`
done
##roop end##

##return to the initial state##
sed -e "s/<=$value2/<=$start1/g" random-forest-onehot.py | sed -e "s/>=$value3/>=$start2/g" | sed -e "s/>$value2/>$start1/g" | sed -e "s/<$value3/<$start2/g" | sed -e "s/confusion_matrix${mat1}.jpg/confusion_matrix1.jpg/g" | sed -e "s/importance${mat1}.csv/importance1.csv/g" | sed -e "s/classification_report${mat1}.csv/classification_report1.csv/g" > random-forest-onehot-new.py
mv random-forest-onehot-new.py random-forest-onehot.py


