 
# Import all from module socket
from socket import *
from thread import *
 
# Defining server address and port
host_a = ''  #'localhost' or '127.0.0.1' or '' are all same
host_b = ''
port_a = 52001 #Use port > 1024, below it all are reserved
port_b = 52002
 
#Creating socket object
sock_a = socket(AF_INET,SOCK_STREAM)
sock_b = socket(AF_INET,SOCK_STREAM)
#Binding socket to a address. bind() takes tuple of host and port.
sock_a.bind((host_a, port_a))
sock_b.bind((host_b, port_b))
#Listening at the address
sock_a.listen(2) #5 denotes the number of clients can queue
sock_b.listen(2) 

def clientthread_a(conn_a):
#infinite loop so that function do not terminate and thread do not end.
     while True:
#Sending message to connected client
         conn_a.send('1\n') #send only takes string
#Receiving from client
         data_a = conn_a.recv(1024) # 1024 stands for bytes of data to be received
         print data_a

def clientthread_b(conn_b):
#infinite loop so that function do not terminate and thread do not end.
     while True:
#Sending message to connected client
         conn_b.send('2\n') #send only takes string
#Receiving from client
         data_b = conn_b.recv(1024) # 1024 stands for bytes of data to be received
         print data_b
 
while True:
#Accepting incoming connections
    conn_a, addr_a = sock_a.accept()
    conn_b, addr_b = sock_b.accept()	
#Creating new thread. Calling clientthread function for this function and passing conn as argument.
    start_new_thread(clientthread_a,(conn_a,)) #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread_b,(conn_b,))
 
conn_a.close()
sock_a.close()
conn_b.close()
sock_b.close()
