#!/bin/sh

for num in `seq 1 31`
do
cut -f 3 --delim="," importance${num}.csv > importance${num}b.csv 
cut -f 2 --delim="," importance${num}.csv > importance${num}c.csv 
paste -d "," importance${num}b.csv importance${num}c.csv > importance${num}d.csv
sort -r importance${num}d.csv > importance${num}e.csv
rm importance${num}b.csv importance${num}c.csv importance${num}d.csv
done
