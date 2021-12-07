#!/bin/sh
"""Usage: sh prepare.sh
Options:

Example:
 sh prepare.sh
"""

#parameters
input=MOS2E04200322RAW
sttime="2020-08-06 10:55:00.000"
edtime="2020-08-06 11:55:00.000"
name=edited2
###############################

#extract a specific time range
st=`grep -n "${sttime}" ${input}-time.csv | sed -e 's/:.*//g'`
ed=`grep -n "${edtime}" ${input}-time.csv | sed -e 's/:.*//g'` 
sed -n ${st},${ed}p ${input}.csv > ${input}-${name}.csv
echo ${input}
echo ${sttime} 
echo ${edtime} 

