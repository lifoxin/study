#!/usr/bin/env python3

import socket
import urllib.request
import urllib.error
try:
    r = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
       print('time out')
