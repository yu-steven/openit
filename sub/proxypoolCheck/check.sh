#!/bin/bash

echo -e "proxypoolCheck\n"
echo "download proxypoolCheck..."
wget https://github.com/yu-steven/proxypoolCheck/releases/download/v0.3.1/proxypoolCheck-linux-amd64 -O proxypoolcheck
echo "done"
echo "chmod 授予777权限..."
chmod +755 proxypoolcheck
echo "done"
echo "静默执行程序，默认配置..."
nohup ./proxypoolcheck -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/proxypoolCheck/check.yaml > /dev/null 2>&1 &
echo "这个进程的PID是..."
