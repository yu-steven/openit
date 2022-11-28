#!/usr/bin/env sh
#Python 3.x
#pwd /path/to/openit/utils/clashcheck
#with log ↓          #no log ↓ 
#nohup ./start.sh &  #nohup ./start.sh > /dev/null 2>&1 &
#TODO start apache if in docker & start clashcheck with while if no false

if [ "$in_docker" = "true" ]; then apachectl start; else echo "Hello"; fi
while [ $? -eq 0 ]; do python main.py; done
