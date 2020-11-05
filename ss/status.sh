#!/bin/bash

ps -ef | grep -v grep | grep ssserver >> /dev/null 2>&1

if [ $? -eq 0 ]
then
    echo "server is running"
else
    echo "server was stoped"
fi
