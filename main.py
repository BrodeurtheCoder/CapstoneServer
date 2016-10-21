import socket, sys, time    # Import socket module
from serializer import serializer

s = socket.socket()
host = "0.0.0.0"
port = 2000

s.listen(5)

while True:
	c, addr = s.accept()
	received = c.recv(1024)
	print "Server received %s" %received

