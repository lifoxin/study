#!/usr/bin/env python3

import socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))

while True:
    st = input('input command: ')
    if not st:break
    s.send(st.encode('utf-8'))
    
    echo_back = s.recv(1024)
    print(echo_back.decode('utf-8'))
 
s.close()
