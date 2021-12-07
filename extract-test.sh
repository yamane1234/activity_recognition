#!/bin/sh
"""Usage: sh extract-test.sh
Options:

Example:
 sh extract-test.sh
"""

#parameters
input2=1012_V1R3XP_4RAW
number=1012
#######################

#set input4
ls $input2.csv > info.txt
n=7
num=`cut -b $n info.txt` #if input2=1000_V1R3XP_4RAW, the results are num=1 and input4=class-info1.txt
input4=class-info$num.txt
rm info.txt

echo $input2
echo "visit$num"
input3=class.txt
value1=1
value2=2

#set an initial parameter of extract.py
value3=`sed -n ${value1}p $input4` #extract the line of $value1 in class-info$num.txt and set it as the variable value3.
value4=`sed -n ${value2}p $input4` #extract the line of $value2 in class-info$num.txt and set it as the variable value4.
sed -e s/cla=1/cla=$value3/g extract.py > extract-new.py #replace cla=1 in extact.py with cla=$value3.
mv extract-new.py  extract.py

##roop starts##
while [ $value1 -lt 11 ]  #while value1 is smaller than 11
do
value3=`sed -n ${value1}p $input4` #extract the line of $value1 in class-info$num.txt and set it as the variable value3.
value4=`sed -n ${value2}p $input4` #extract the line of $value2 in class-info$num.txt and set it as the variable value4.
echo "$value1"
echo "class:$value3"
mkdir -p Features/$input2/$value1 #make a directory

#extract only acceleration values
sed -e "1,10d" $input2.csv > $input2-edited.csv

#add time 
grep "Start Time" $input2.csv | cut -b 12- > start-download.txt     #Start time of data acquisition
grep "Download Time" $input2.csv | cut -b 15- >> start-download.txt #End time of data acquisition
python time.py
wait
rm $input2-edited.csv start-download.txt 

#add classification and cut out data.
echo "Extraction"
python extract.py
wait
rm $input3 $input2-time.csv $input2-time-class-combined.csv  

#Process data that were cut out every 10 seconds without overlapping
count=`ls $input2-time-cut-class-*.csv | wc -l`
count2=$((($count * 10)-10))
echo "$count2"

for i in `seq 0 10 $count2` 
do
cut -d "," -f 3,5- $input2-time-cut-class-${i}.csv > $input2-class-${i}A.csv
rm $input2-time-cut-class-${i}.csv
done

#calculate features
for i in `seq 0 10 $count2`
do
python features.py < $input2-class-${i}A.csv
mv features.csv features-${i}A.csv
echo "Feature calculation data set ${i}"
done

python iqr.py  #calculate IQR
python arc_p4.py #calculate ARC(p=4)
wait

rm $input2-time-cut.csv #delete this as it will not be used any more

for i in `seq 0 10 $count2`
do
echo "edit ARC ${i}"
sed -n 1,7p arc_p4-${i}A.csv | xargs >> arc_p4-${i}A-2.csv
sed "s/ /,/g" arc_p4-${i}A-2.csv > arc_p4-${i}A-3.csv #convert spaces to commas
rm arc_p4-${i}A.csv
done

for i in `seq 0 10 $count2`
do 
echo "integrate ${i}"
echo "${number}" > number.txt
paste -d "," number.txt features-${i}A.csv iqr-${i}A.csv arc_p4-${i}A-3.csv > features-${value1}-${i}A.csv
rm number.txt features-${i}A.csv iqr-${i}A.csv arc_p4-${i}A-2.csv arc_p4-${i}A-3.csv #delete the files used for the integration
STR=`cat features-${value1}-${i}A.csv`
if [ "`echo $STR | grep error`" ] ; then rm features-${value1}-${i}A.csv; fi #delete files containing error
mv features-${value1}-${i}A.csv Features/$input2/$value1 #move
done

rm $input2-class-*A.csv 
sed -e s/cla=$value3/cla=$value4/g extract.py | sed -e s/start$value1/start$value2/g | sed -e s/stop$value1/stop$value2/g > extract-new.py
mv extract-new.py  extract.py
value1=`echo $(($value1+1))`
value2=`echo $(($value2+1))`
done
##roop ends##

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
