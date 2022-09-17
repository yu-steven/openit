#!/bin/bash
name=Openit
line=`wc -l < url`
time=`date '+%Y.%m.%d %H:%M:%S'`

echo -e "REMARKS=$name \nSTATUS=节点数量: $line.♥.更新时间: $time"
