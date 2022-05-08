#!/bin/bash

echo -e "proxypoolcheck\n"
echo "download proxypoolcheck.gz..."
wget https://github.com/Sansui233/proxypoolCheck/releases/download/v0.3.1/proxypoolCheck-linux-amd64-v0.3.1.gz -O proxypoolcheck.gz
echo "done"
echo "unzip proxypoolcheck.gz..."
gzip -d proxypoolcheck.gz
echo "done"
echo "chmod 授予777权限..."
chmod +755 proxypoolcheck
echo "done"
echo "静默执行程序,默认配置..."
nohup ./proxypoolcheck -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/check.yaml
