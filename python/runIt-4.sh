#!/bin/sh
set -x
if pgrep "$0"; then
#if ps -ef | grep -v grep | grep coinTrader ; then
	echo "Already running"
        exit 0
else
	cd /home/ec2-user/coinTrader && /usr/bin/python /home/ec2-user/coinTrader/coinTrader-4.py >> /home/ec2-user/coinTrader/log/coinTrader-4.log 2>&1
        exit 0
fi
