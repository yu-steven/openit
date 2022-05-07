#!/bin/bash

echo -e "proxypool\n"
echo "下载 proxypool"
wget https://github.com/daycat/proxypool/releases/download/latest/proxypool-linux-amd64 -O proxypool
echo "chmod 授予777权限"
chmod 777 proxypool
echo "静默执行程序，默认配置"
nohup ./proxypool -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/config.yaml
