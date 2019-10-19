#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 2999)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    message = './script.sh www.usec.io Security'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()