#!/usr/bin/env python3

import socket


sd = socket.socket(type=socket.SOCK_DGRAM)

while True:
    
    data = input("发送: ")

    if data == 'q':
        break

    sd.sendto(data.encode(),('127.0.0.1',9000))
    
sd.close()


