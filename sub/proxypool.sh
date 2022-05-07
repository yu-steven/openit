#!/bin/bash

echo -e "proxypool\n"
echo "下载 proxypool"
wget https://github.com/daycat/proxypool/releases/download/latest/proxypool-linux-amd64 -O proxypool
echo "chmod 授予777权限"
chmod 777 proxypool
echo -e "静默执行程序，默认配置\n结果会输出到12580端口"
nohup ./proxypool -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/config.yaml
