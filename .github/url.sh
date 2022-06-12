#!/bin/bash
name=Openit
line=`sed -n '$=' url`
time=`date "+%Y.%m.%d %H:%M:%S"`
url=$[line-2]

echo -e "REMARKS=$name \nSTATUS=节点数量: $url.♥.更新时间: $time"
