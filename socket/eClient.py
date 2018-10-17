import socket 

s = socket.socket()

host = socket.gethostname()
port = 2006

s.connect((host,port))

while(True):
	data = s.recv(1024)
	print("Data received from server : ",data)

	data = input("Enter the data to send to server")
	s.send(data.encode())

	c = int(input("Do you want to continue:"))
	if c == -1:
		break
s.close()
