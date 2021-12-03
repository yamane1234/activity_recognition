#!/bin/sh

#parameters
#input=MOS2E02200116RAW
#input=MOS2E02200125RAW
input=MOS2E04200322RAW
#input=MOS2E02200126RAW
sttime="2020-08-06 10:55:00.000"
edtime="2020-08-06 11:55:00.000"
name=edited2

#特定の時間範囲の箇所を抽出
st=`grep -n "${sttime}" ${input}-time.csv | sed -e 's/:.*//g'`
ed=`grep -n "${edtime}" ${input}-time.csv | sed -e 's/:.*//g'` 
sed -n ${st},${ed}p ${input}.csv > ${input}-${name}.csv
echo ${input}
echo ${sttime} 
echo ${edtime} 

#paste -d "," MOS2E04200322RAW-edited2.csv MOS2E02200126RAW-edited2.csv > 1003_V1R3XP_4RAW.csv 
#vi 1003_V1R3XP_4RAW.csv
