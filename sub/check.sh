#!/bin/bash

echo -e "proxypoolcheck\n"
echo "下载 proxypoolcheck.gz"
wget https://github.com/Sansui233/proxypoolCheck/releases/download/v0.3.1/proxypoolCheck-linux-amd64-v0.3.1.gz -O proxypoolcheck.gz
echo "解压 proxypoolcheck.gz"
gzip -d proxypoolcheck.gz
echo "删除 proxypoolcheck.gz"
rm proxypoolcheck.gz
echo "chmod 授予777权限"
chmod 777 proxypoolcheck
echo "静默执行程序,默认配置"
nohup ./proxypoolcheck -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/check.yaml
