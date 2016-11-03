import socket, sys, time    # Import socket module


# need to find a way to automatically boot capstone server code 
# so that it only needs to be done once and runs continuously


s = socket.socket()
host = "0.0.0.0"
port = 2000

s.bind((host, port))
s.listen(5)

#print "Messages received from pi sent as [time, data] \n"


while c, addr != s.accept()
print "Server accepted conncetion from node"

while True:
	#receivedMessage = c.recv(1024)
	#print "receivedMessage: " + receivedMessage
	received = c.recv(1024)
	print "Server received ", received
