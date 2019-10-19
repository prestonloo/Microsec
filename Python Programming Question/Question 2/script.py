#!/usr/bin/python

import socket
import sys
from struct import *

s = socket.socket(socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))

while True:
	packet = s.recvfrom(65565)
	packet = packet[0]
	ip_header = packet[0:20]
	iph = unpack('!BBHHHBBH4s4s' , ip_header)
	s_addr = socket.inet_ntoa(iph[8])
	d_addr = socket.inet_ntoa(iph[9])
	
	print ("Source Address : " + str(s_addr) + " Destination Address : " + str(d_addr))
	
	version_ihl = iph[0]
	version = version_ihl >> 4
	ihl = version_ihl & 0xF
	iph_length = ihl * 4
	tcp_header = packet[iph_length:iph_length+20]
	tcph = unpack('!HHLLBBHHH' , tcp_header)	
	source_port = tcph[0]
	dest_port = tcph[1]

	print ("Source Port : " + str(source_port) + " Destination Port : " + str(dest_port))