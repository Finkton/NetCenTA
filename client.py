import socket 
def Main(): 
	ip='127.0.0.1' 
	port=8000 

	s = socket.socket() 
	s.connect((ip,port))
	
	print("connection established")
	while True:
		query = raw_input("text to server => ") 
		s.send(query)
		string = s.recv(1024)
		print string

	s.close()

if __name__=="__main__":
	Main()
