#!/usr/bin/env python3
__author__ = "Silverback"

import socket

host = 'data.pr4e.org'
port = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( (host, port))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()