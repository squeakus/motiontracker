#!/bin/bash
if [ $# -lt 1 ];
then
    echo "please specify detector: reundetector.sh <sift|surf|orb|brisk|akaze>"
    exit 0
fi

source /home/pi/.virtualenvs/cv/bin/activate
echo  "runnning with $1 detector"
python /home/pi/motiontracker/showdetector.py -p 1 -d $1

