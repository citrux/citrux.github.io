#!/bin/bash

start=$1
end=$2

for i in $(seq $start $end); do
    p=$(python3 110.py $i)
    q=$(python3 110_constructive.py $i)
    if [[ $p != $q ]]; then
        echo "$i: $p != $q"
    else
        echo "$i: $p == $q"
    fi
done
