
import socket               # Import socket module
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'
         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

s.close                     # Close the socket when done




