#!/bin/bash

time1=`date "+%Y-%m-%d %H:%M:%S"`
time2=`date "+%H:%M"`
time3="22:30"
server=`ps -ef | grep -v grep |grep shadowsocks`
main(){
if [ -z "$server" ]
then
	echo "$time1 server had failed and now restart" >> /tmp/normal.time
	/bin/ssserver -c /home/felix/jj.json >> /tmp/jj.log 2>&1 &
	echo "$time2 server restart"
else
	echo "$time1 jj is running" >> /tmp/normal.time
	echo "$time2 server running"
fi
}
iftime(){
if [ $time2 = $time3 ]
then
	pid=`ps -ef |grep shadowsocks |grep -v grep |awk '{print $2}'`
	echo "it's time to stop server"
	echo "$time1 is time to stop server" >> /tmp/error.time
	kill -9 $pid
	exit 0
else
	echo "$time2 is not 22:30"
fi
}
sleep 3
#iftime
sleep 3
main
echo "All is ok"
exit 0
