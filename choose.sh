#!/bin/sh
"""Usage: sh choose.sh
Options:

Example:
 sh choose.sh 
"""

#parameters
value1=1000
value2=1046 #note that this value is not included in the processing range.
choice=54  #how many to select from each data
##########

rm -r temp/* #delete temp/*
rm f.csv #delete old f.csv.

while [ $value1 -lt $value2 ]   #execute loop as long as the value is less than value2.
do
echo "$value1"
mkdir -p ./temp/${value1}

for i in `seq 1 10`   #assign sequentially 1,2,3,...,8,9,10:classify 10 activities
do
echo "$i"
#randomly select $choice of files in the folder and copy them. 
find Features/${value1}_V1R3XP_4RAW/${i}/ | grep csv | sort -R | head -n ${choice} | xargs -n 1 sh -c 'cp -v $0 ./temp/'
#move files
mv ./temp/*.csv ./temp/${value1}
done

#integrate files
cat ./temp/${value1}/* >> f.csv #add to the existing f.csv
value1=`echo $(($value1+1))`
done

#add labels in the first line.
sed -e "1i ID,Class,mean1,mean2,mean3,mean4,mean5,mean6,stdev1,stdev2,stdev3,stdev4,stdev5,stdev6,variance1,variance2,variance3,variance4,variance5,variance6,max1,max2,max3,max4,max5,max6,min1,min2,min3,min4,min5,min6,rms1,rms2,rms3,rms4,rms5,rms6,sma_hip,sma_wrist,corr13,corr12,corr23,corr46,corr45,corr56,entropy1,entropy2,entropy3,entropy4,entropy5,entropy6,energy1,energy2,energy3,energy4,energy5,energy6,kurtosis1,kurtosis2,kurtosis3,kurtosis4,kurtosis5,kurtosis6,skewness1,skewness2,skewness3,skewness4,skewness5,skewness6,median1,median2,median3,median4,median5,median6,iqr1,iqr2,iqr3,iqr4,iqr5,iqr6,arc1-1,arc1-2,arc1-3,arc1-4,arc2-1,arc2-2,arc2-3,arc2-4,arc3-1,arc3-2,arc3-3,arc3-4,arc4-1,arc4-2,arc4-3,arc4-4,arc5-1,arc5-2,arc5-3,arc5-4,arc6-1,arc6-2,arc6-3,arc6-4" f.csv > features_edited.csv

