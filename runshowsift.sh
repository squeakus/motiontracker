#!/bin/bash


source /home/pi/.virtualenvs/cv/bin/activate
echo "env:" $VIRTUAL_ENV
sleep 5
python /home/pi/Desktop/showsift.py -p 1

