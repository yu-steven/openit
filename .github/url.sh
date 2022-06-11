#!/bin/bash
time=`date "+%Y.%m.%d %H:%M:%S"`
line=`sed -n '$=' url`
url=$[line-2]

echo -e "REMARKS=Openit \nSTATUS=节点数量: $url.♥.更新时间: $time"
