import socket, sys, time    # Import socket module

# need to find a way to automatically boot capstone server code 
# so that it only needs to be done once and runs continuously

print "Hello world"
s = socket.socket()
host = "0.0.0.0"
port = 2000

s.bind((host, port))
s.listen(1)

c, addr = s.accept()
print "Server accepted connection from node"
c.send("hello world")

#while True:
#	print "in while loop looking to receive"
#	received = c.recv(1024)
#	print "Server received: ", received
#	if received == "quit":
#		break
#s.close()
#c.close()	

while True:
    data = c.recv(1024)
    print "received data: ", data
    if data == "quit":
	break
c.close()
s.close()
