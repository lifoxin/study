#!/bin/bash

time1=`date "+%Y-%m-%d %H:%M:%S"`
kill -9 $(ps -ef |grep -v grep |grep ssserver|awk '{print $2}') >> /dev/null 2>&1

#-ne != 
#-eq  =
if [ $? -eq 0 ] 
then
    echo "$time1 >> the service has been shut down" >> /tmp/error.time
    echo "$time1 >> the service has been shut down" 
else
    echo "$time1 >> the service did not start" >> /tmp/error.time
    echo "$time1 >> the service did not start"
fi
