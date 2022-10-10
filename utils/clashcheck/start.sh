#!/bin/sh
#python 3.x
#pwd /home/$USER/clashcheck
#with log ↓          #no log ↓ 
#nohup ./start.sh &  #nohup ./start.sh > /dev/null 2>&1 &
#TODO start clashcheck with while

while true
do
  pkill -9 clash-
  /usr/bin/timeout -k 20 4m /usr/bin/python main.py
done
