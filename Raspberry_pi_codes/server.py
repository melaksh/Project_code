			#Echo Server Program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 52033              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
#print 'hello';
conn, addr = s.accept()
#print 'hello';
print 'Connected by', addr
while 1:
	#data = conn.recv(1024)
	#print data;
        #if not data: break
        conn.sendall("Sent by server\n")
conn.close()
