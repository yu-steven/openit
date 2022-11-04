#!/bin/sh
#python 3.x
#pwd /home/$USER/clashcheck
#with log ↓          #no log ↓ 
#nohup ./start.sh &  #nohup ./start.sh > /dev/null 2>&1 &
#macOS -> `zsh: command not found: timeout` -> https://stackoverflow.com/questions/3504945/timeout-command-on-mac-os-x
#TODO start apache & start clashcheck with while

apachectl start || true
while [ $? -eq 0 ]; do timeout -k 20 4m python main.py; done
