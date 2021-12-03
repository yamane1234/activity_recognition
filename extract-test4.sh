#!/bin/sh

#parameter(input2)
input2=1012_V1R3XP_4RAW
number=1012
#######################

#set input4
ls $input2.csv > info.txt
n=7
num=`cut -b $n info.txt` #input2=1000_V1R3XP_4RAWならnum=1になり、input4=class-info1.txtとなる。
input4=class-info$num.txt
rm info.txt

echo $input2
echo "visit$num"
input3=class.txt
value1=1
value2=2

#set an initial parameter of extract.py
value3=`sed -n ${value1}p $input4` #class-info$num.txtの$value1行目を抽出し、変数value3とする。
value4=`sed -n ${value2}p $input4`
sed -e s/cla=1/cla=$value3/g extract.py > extract-new.py #extact.pyのcla=1をcla=$value3に置き換える。
mv extract-new.py  extract.py

##roop starts##
#while [ $value1 -lt 7 ]
while [ $value1 -lt 11 ]  #value1が11より小さい間
do
value3=`sed -n ${value1}p $input4` #class-info$num.txtの$value1行目を抽出し、変数value3とする。
value4=`sed -n ${value2}p $input4`
echo "$value1"
echo "class:$value3"
mkdir -p Features/$input2/$value1 #directoryを作る

#加速度の値のみ抽出
sed -e "1,10d" $input2.csv > $input2-edited.csv

#時間を追加
grep "Start Time" $input2.csv | cut -b 12- > start-download.txt     #データ取得開始時間
grep "Download Time" $input2.csv | cut -b 15- >> start-download.txt #データ取得終了時間
python time.py
wait
rm $input2-edited.csv start-download.txt 
#exit
#分類を追加してデータを切り出す
echo "Extraction"
python extract.py
wait
#rm $input3 $input2-time.csv $input2-time-class-combined.csv $input2-time-cut.csv $input2-time-cut2.csv 
rm $input3 $input2-time.csv $input2-time-class-combined.csv  

#non-overlappingで10秒ごとに切り出したデータの加工
count=`ls $input2-time-cut-class-*.csv | wc -l`
count2=$((($count * 10)-10))
echo "$count2"

#for i in `seq 0 10 50` 
for i in `seq 0 10 $count2` 
do
#cut -d "," -f 4,6- $input2-time-cut-class-${i}.csv > $input2-class-${i}A.csv
cut -d "," -f 3,5- $input2-time-cut-class-${i}.csv > $input2-class-${i}A.csv
rm $input2-time-cut-class-${i}.csv
done

#特徴量を計算
#for i in `seq 0 10 50`
for i in `seq 0 10 $count2`
do
python features.py < $input2-class-${i}A.csv
mv features.csv features-${i}A.csv
echo "Feature calculation data set ${i}"
done

python iqr.py  #calculate IQR
python arc_p4.py #calculate ARC(p=4)
wait

rm $input2-time-cut.csv #これ以上は使用しないので削除

for i in `seq 0 10 $count2`
do
echo "edit ARC ${i}"
sed -n 1,7p arc_p4-${i}A.csv | xargs >> arc_p4-${i}A-2.csv
sed "s/ /,/g" arc_p4-${i}A-2.csv > arc_p4-${i}A-3.csv #スペース(空白)をカンマ(,)に変換
rm arc_p4-${i}A.csv
done

for i in `seq 0 10 $count2`
do 
echo "integrate ${i}"
echo "${number}" > number.txt
#paste -d "," features-${i}A.csv iqr-${i}A.csv arc_p4-${i}A-2.csv > features${i}A.csv
#paste -d "," features-${i}A.csv iqr-${i}A.csv arc_p4-${i}A-3.csv > features-${value1}-${i}A.csv
paste -d "," number.txt features-${i}A.csv iqr-${i}A.csv arc_p4-${i}A-3.csv > features-${value1}-${i}A.csv
rm number.txt features-${i}A.csv iqr-${i}A.csv arc_p4-${i}A-2.csv arc_p4-${i}A-3.csv #統合に使用したファイルを削除
#sed '/error/d' features${i}A.csv > features-${value1}-${i}A.csv #errorを含む行を削除
STR=`cat features-${value1}-${i}A.csv`
if [ "`echo $STR | grep error`" ] ; then rm features-${value1}-${i}A.csv; fi #errorを含むfilesを削除
mv features-${value1}-${i}A.csv Features/$input2/$value1 #移動
done

#count3=$((1 + 6 * ($count - 1)))
#echo "$count3"
#for i in `seq 1 6 31`  #1,7,13,19,25,31を代入していく
#for i in `seq 1 6 $count3`  #1,7,13,19,25,31,...を代入していく
#do
#echo "edit ARC ${i} $((${i}+5))"
#sed -n ${i},$((${i}+5))p arc_p4.csv | xargs >> arc_p4-2.csv #arc_p4.csvを6行ごとに1行にして既存のファイルに追加
#done
 
rm $input2-class-*A.csv 
#rm arc_p4.csv
sed -e s/cla=$value3/cla=$value4/g extract.py | sed -e s/start$value1/start$value2/g | sed -e s/stop$value1/stop$value2/g > extract-new.py
mv extract-new.py  extract.py
value1=`echo $(($value1+1))`
value2=`echo $(($value2+1))`
done
##roop ends##

##integrate##
#paste -d "," features.csv iqr.csv arc_p4-2.csv > features2.csv
#sed '/error/d' features2.csv > features3.csv #errorを含む行を削除
#sed -e "1i Class,mean1,mean2,mean3,mean4,mean5,mean6,stdev1,stdev2,stdev3,stdev4,stdev5,stdev6,variance1,variance2,variance3,variance4,variance5,variance6,max1,max2,max3,max4,max5,max6,min1,min2,min3,min4,min5,min6,rms1,rms2,rms3,rms4,rms5,rms6,sma_hip,sma_wrist,corr13,corr12,corr23,corr46,corr45,corr56,entropy1,entropy2,entropy3,entropy4,entropy5,entropy6, energy1,energy2,energy3,energy4,energy5,energy6,kurtosis1,kurtosis2,kurtosis3,kurtosis4,kurtosis5,kurtosis6,skewness1,skewness2,skewness3,skewness4,skewness5,skewness6,median1,median2,median3,median4,median5,median6,iqr1,iqr2,iqr3,iqr4,iqr5,iqr6,arc1-1,arc1-2,arc1-3,arc1-4,arc2-1,arc2-2,arc2-3,arc2-4,arc3-1,arc3-2,arc3-3,arc3-4,arc4-1,arc4-2,arc4-3,arc4-4,arc5-1,arc5-2,arc5-3,arc5-4,arc6-1,arc6-2,arc6-3,arc6-4" features3.csv > features_edited.csv
#rm features2.csv features3.csv
 
#move the input file to a directry
directory="Processed"
if [ -d "$directory" ]; then
   mv $input2.csv Processed
else
   mkdir $directory
   mv $input2.csv Processed
fi

#reset the parameters of extract.py
sed -e s/cla=$value4/cla=1/g extract.py | sed -e s/start$value1/start1/g | sed -e s/stop$value1/stop1/g > extract-new.py
mv extract-new.py  extract.py
