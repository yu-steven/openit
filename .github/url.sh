#!/bin/bash
name=Openitsub
line=$(expr $(wc -l < url) + 1)
time=$(date '+%Y.%m.%d %H:%M:%S')

echo "$time >>> $line" >> .github/log && sed -i '2d' .github/log
echo -e "REMARKS=$name \nSTATUS=节点数量: $line.♥.更新时间: $time"
