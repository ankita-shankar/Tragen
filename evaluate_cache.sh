#!/bin/bash
max=8
size=1
log_interval=3
for (( i=1; i <= $max; ++i ))
do
    #go from 1GB to 8GB in cache size
    size=`expr $i \* 1000`
    tmp=$(mktemp)
    jq ".cache_config.cacheSizeMB=${size}" config.json  > "$tmp" && mv "$tmp" config.json
    cat config.json
    ./../../../CacheLibPrivate/opt/cachelib/bin/cachebench --progress $log_interval --json_test_config config.json --progress_stats_file results/progress/cache_size_${size}.txt > results/final/cache_size_${size}.txt
    echo $size
done
