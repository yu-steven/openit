#!/bin/bash
status_log=$(git status -sb)
# 这里使用的是 main 分支，根据需求自行修改
if [ "$status_log" == "## main...origin/main" ];then
  echo -e "\033[42;30m nothing to commit, working tree clean \033[0m"
else
  git pull origin main && git add . && git commit -m "$(date '+%Y.%m.%d %H:%M:%S') 更新订阅" && git push origin main
fi
