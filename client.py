
import socket               # Import socket module
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'
         
host = socket.gethostname()
port = 5182                # Reserve a port for your service.

s.connect((host, port))
data="hello\n"


 
#Bind socket to local host and port
try:
    s.sendall(data)
except socket.error as msg:
    print 'Bind failed. Error in Message sending!'
    sys.exit()

print 'Message Sent '
print s.recv(1024)

s.close                     # Close the socket when done




