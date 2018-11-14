#!/usr/bin/env python3

import socket

sd = socket.socket(type=socket.SOCK_DGRAM)
sd.bind(('0.0.0.0', 9000))

while True:

    data, addr = sd.recvfrom(1024)

    print("接收数据来源：%s，内容：%s"%(addr,data.decode()))

sd.close()



