#!/bin/bash

echo -e "proxypool\n"
echo "download proxypool..."
wget https://github.com/yu-steven/proxypool/releases/download/v0.6.1/proxypool-linux-amd64 -O proxypool
echo "done"
echo "chmod 授予777权限..."
chmod +777 proxypool
echo "done"
echo -e "静默执行程序，默认配置...\n结果会输出到12580端口"
nohup ./proxypool -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/config.yaml
