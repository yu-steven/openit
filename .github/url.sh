#!/bin/bash


time=`date "+%Y.%m.%d %H:%M:%S"`
line=`sed -n '$=' url`

echo -e "REMARKS=Openit \nSTATUS=节点数量: $line.♥.更新时间: $time"
