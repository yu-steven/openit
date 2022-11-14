#!/bin/sh
#python 3.x
#pwd /home/$USER/clashcheck
#with log ↓          #no log ↓ 
#nohup ./start.sh &  #nohup ./start.sh > /dev/null 2>&1 &
#TODO start apache if exist & start clashcheck with while if no false
#macOS -> `zsh: command not found: timeout` -> https://stackoverflow.com/questions/3504945/timeout-command-on-mac-os-x
#                         | --------- ↑
apachectl start || true # ↓
while [ $? -eq 0 ]; do timeout -k 20 4m python main.py; done
