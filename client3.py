import socket               # Import socket module
import sys
import os
from thread import *
 

s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.
 
s.connect((host, port))
name = raw_input("Enter Your Name --->>> ")
s.send(name)
print s.recv(1024)

def rec():
    while True:  
        #Receiving from client        
	data = s.recv(1024)
        print data
start_new_thread(rec,())
while 1:		
	msg = raw_input()
	if msg.lower()=='list':
		os.system('clear')
		s.send(' list')				
	else:	
		name1,reply = msg.split(' ',1)		
		s.send(name1 +' '+name+' : '+reply)
	if not reply:
		break
	
