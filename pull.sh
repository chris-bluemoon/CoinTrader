#!/bin/bash
IP=$1
echo $IP
scp -i /Users/chrismilner/myKeyPairs/bluemoon.pem ec2-user@${IP}:coinTrader/* /Users/chrismilner/coinTrader/
