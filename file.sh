#!/bin/sh
"""Usage: sh file.sh
Options:

Example:
sh file.sh
"""

#parameters
raw="raw" 
input="MOS2E04200322RAW"
###########################

#extract a specific time range by executing date.py and prepare.sh 
echo ${raw}
echo ${input}
tail -n +12 ${raw} > ${input}.csv  #use only axis values
sed -i '1s/^/Axis1,Axis2,Axis3\n/' ${input}.csv #add Axis1, Axis2, Axis3 to the first line
python date.py
wait
sh prepare.sh
rm ${raw}
