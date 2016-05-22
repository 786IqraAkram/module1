
from socket import *
from threading import Thread
import sys

HOST = ''
PORT = 5188
ADDR = (HOST, PORT)
S = socket(AF_INET, SOCK_STREAM)
S.connect((HOST, PORT))
def recv():

    while True:

        data = S.recv(1024)

        if not data: sys.exit(0)

        print data



Thread(target=recv).start()

while True:

    data = raw_input('>>> ')
    S.send(data)
    
S.close()




