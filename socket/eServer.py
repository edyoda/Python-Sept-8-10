# Socket programming : 

# request.get() = > socket => server socket 

# ip : 145.45.78.45 port : 80 => zekelabs.com
# ip : 145.45.78.45 port : 8080  => dev server  

# FTP : port 30
# SMTP : 25


# Server 


# 1 identify the server ip address and port number 

# 2 socket and bind ip address and port no   
# 	bind(145.78.45.65,52)

# 3 listen : 

# 4 accept 

# 5 send/recv = > bytes  


# Connect :

# 1 ip ,port 

# 2 connect 

# 3 send/recv

# TCP => three step hanshaking =>  ack to cleint => server => client  
# UDP 

# Host : 
#    1 gethostname => localhost 
#    2 getfqdn =>  ip addr
#    3 gethostbyname => url  



import socket 

s = socket.socket()

host = socket.gethostname()
port = 2006

s.bind((host,port))

s.listen(5)


c =  0
while(True):
	client_socket,client_addr = s.accept()
    print(client_socket,client_addr)

	data = input("Enter the data to send it to client")
	client_socket.send(data.encode())
	data = client_socket.recv(1024)
	print("Data from client",data)

	c = int(input("do you want to continue"))

	if c == -1:
		break
client_socket.close()
s.close()