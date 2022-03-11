#!/bin/bash
status_log=$(git status -sb)
# 这里使用的是 main 分支，根据需求自行修改
if [ "$status_log" == "## main...origin/master" ];then
  echo "nothing to commit, working tree clean"
else
  git add .&&git commit -m "Collected by GitHub action"&&git push origin master
fi
