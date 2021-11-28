#!/bin/bash
max=10
size=1
for (( i=1; i <= $max; ++i ))
do
    #go from 100MB to 10GB in cache size
    size=$i*100
    tmp=$(mktemp)
    jq ".cache_config.cacheSizeMB=${size}" real_trace_config.json  > "$tmp" && mv "$tmp" real_trace_config.json
    ./../CacheLibPrivate/opt/cachelib/bin/cachebench --progress 1 --json_test_config real_trace_config.json --progress_stats_file real_results/progress/cache_size_${size}.txt > real_results/final/cache_size_${size}.txt
done