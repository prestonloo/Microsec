#!/usr/bin/python

import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 2999)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address
        while True:
            data = connection.recv(1024)
            print >>sys.stderr, 'received "%s"' % data
            os.system(data)
            if data != "":
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        connection.close()