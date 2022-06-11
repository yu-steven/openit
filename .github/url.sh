#!/bin/bash
name=Openit
line=`sed -n '$=' url`
url=$[line-2]
time=`date "+%Y.%m.%d %H:%M:%S"`

echo -e "REMARKS=$name \nSTATUS=节点数量: $url.♥.更新时间: $time"
