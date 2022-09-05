#!/bin/bash
#sudo timedatectl set-timezone 'Asia/Shanghai'
#git config pull.rebase false
#git config --local user.name "GitHub Actions"
#git config --local user.email "actions@github.com"
#pip install -r ./utils/pool/requirements.txt
#pip install -r ./utils/clashcheck/requirements.txt
#cd ./utils/rm/ && npm ci

python ./utils/pool/main.py

cp ./utils/pool/output.yaml ./utils/clashcheck/input.yaml
python ./utils/clashcheck/main.py
rm ./utils/clashcheck/input.yaml

mv ./utils/clashcheck/check.yaml ./utils/subconverter/check.yaml
./utils/subconverter/subconverter -g --artifact "clash2base64"
rm utils/subconverter/check.yaml

base64 -d ./utils/subconverter/check > ./utils/rm/url1
cat ./utils/rm/url1 ./sub/url2 > ./utils/rm/url
rm ./utils/subconverter/check ./utils/rm/url1

cd ./utils/rm/
npm start

# url https
cd .
rm ./utils/rm/url
mv ./utils/rm/out ./url
./.github/url.sh > ./1
cp url 2
cat 1 2 > 3 && rm 1 2
base64 3 > https -w 0 && rm 3
base64 ./url > ./utils/subconverter/base64 -w 0
sort url -o url 

# long Clash.yaml
./utils/subconverter/subconverter -g --artifact "clash"
./utils/subconverter/subconverter -g --artifact "long"
mv ./utils/subconverter/Clash.yaml ./Clash.yaml || true #output ./Clash.yaml
mv ./utils/subconverter/long ./long || true #output ./Clash.yaml
rm ./utils/subconverter/base64

# git push
./.github/update-repo.sh || true
