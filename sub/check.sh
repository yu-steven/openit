#!/bin/bash

echo -e "proxypoolcheck\n"
echo "下载proxypoolcheck"
wget https://github.com/Sansui233/proxypoolCheck/releases/download/v0.3.1/proxypoolCheck-linux-amd64-v0.3.1.gz -O proxypoolcheck.gz
echo "解压proxypoolcheck"
gzip -d proxypoolcheck.gz
echo "授予权限"
chmod 777 proxypoolcheck
echo "静默运行程序"
nohup ./proxypoolcheck -c https://raw.githubusercontent.com/yu-steven/openit/main/sub/check.yaml
