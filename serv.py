'''
    Simple socket server using threads
'''
  
import socket
import sys
from thread import *
  
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5188 # Arbitrary non-privileged port

address = []
name=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
  
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
      
print 'Socket bind complete'
  
#Start listening on socket
s.listen(10)
print 'Socket now listening'
  
#Function for handling connections. This will be used to create threads

def clientthread(conn):
    #Sending message to connected client
    data1=conn.recv(1024)
    name.append(data1)
    for i in range(len(name)-1):
	address[i].sendall(data1 + ' is online for chat :')	
    conn.send('Welcome to the server. online clients are : \n') #send only takes string
    for i in range(len(name)):
	conn.send(name[i] + '\n')
    #infinite loop so that function do not terminate and thread do not end.
    while True:  
        #Receiving from client
	data = conn.recv(1024)
	to,reply=data.split(' ',1)
	if reply.lower() == "list":	
		conn.send('Available Clients are  : \n')		
		for index in range(len(name)):
			conn.sendall(name[index])
			conn.sendall('\n')
		
	else:
		check = 0		
		for x in range(len(name)):
			if to.upper() == name[x].upper():		
				address[x].sendall(reply)
				check = 1
		if check ==0:
			conn.sendall('User is not Available : Typer list to check Users \n')
		
	if not data: 
		conn.sendall('Your client left the chat \n To see list : type :: list ')            
		break
	#came out of loop
    conn.close()
  
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    address.append(conn)
    start_new_thread(clientthread ,(conn,))
 	 
s.close()
