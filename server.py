import socket 
import thread

global var

def func(client, addr):
	print "connected to:  ", addr
	while True:
		string = client.recv(1024)
		print addr," said => ", string
		client.send("ack")


def Main():
	host='127.0.0.1'
	port=8000
	s = socket.socket()
	s.bind((host,port))
	s.listen(10) # max number of connections

	print "Waiting for new connections"
	while True:
		client, addr = s.accept()
		thread.start_new_thread(func,(client,addr))

		
if __name__=="__main__":
	Main()
