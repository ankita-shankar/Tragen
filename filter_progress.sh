#!/bin/bash
rm -rf filtered
mkdir filtered
max=8
for (( i=1; i <= $max; ++i ))
do
    #go from 1GB to 8GB in cache size
    size=`expr $i \* 1000`
    cat progress/cache_size_${size}.txt | grep 'ops completed\|RAM Hit' > filtered/${size}.txt
done
cd filtered
