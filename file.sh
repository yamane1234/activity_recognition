#!/bin/sh

#parameters
#raw='MOS2E02200116 (2020-06-22)RAW.csv'* 
raw="raw" 
input="MOS2E04200322RAW"

#特定の時間範囲の箇所を抽出
echo ${raw}
echo ${input}
tail -n +12 ${raw} > ${input}.csv  #軸の値のみにする
sed -i '1s/^/Axis1,Axis2,Axis3\n/' ${input}.csv #先頭行にAxis1,Axis2,Axis3の1行を追加
#sed -e s/^M// ${input}.csv > t #改行の印を削除
#mv t ${input}.csv
python date.py
wait
sh prepare.sh
rm ${raw}
#paste -d "," MOS2E04200322RAW-edited2.csv MOS2E02200126RAW-edited2.csv > 1003_V1R3XP_4RAW.csv 
#vi 1003_V1R3XP_4RAW.csv
