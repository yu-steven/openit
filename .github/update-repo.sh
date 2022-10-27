#!/bin/bash
status_log=$(git status -sb)
# 这里使用的是 main 分支，根据需求自行修改
if [ "$status_log" == "## main...origin/main" ];then
  echo -e "\033[32m nothing to commit, working tree clean \033[0m"
else
  git status -s && git add . && git commit -m "$(date '+%Y.%m.%d %H:%M:%S') 订阅更新" && git pull origin main && git push origin main
fi
