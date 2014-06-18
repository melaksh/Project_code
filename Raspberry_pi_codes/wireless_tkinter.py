from Tkinter import *
from tkMessageBox import *
from socket import *
from thread import *
import string
import time

global root;
global sock;
global host;
global port;
global data;
global entrybox_Port;

#def establish_connection():
	#host = '';  #'localhost' or '127.0.0.1' or '' are all same
	#port = 52002;
	#sock = socket(AF_INET,SOCK_STREAM);
	#sock.bind((host, port));
	#sock.listen(2);
 
def create_Port(root):
	global entrybox_Port;
	Label(root, text="Port").pack(fill=X);
	entrybox_Port = Entry(root);
	entrybox_Port.pack(fill=X);	

def create_IP_Entrybox(root):
	global entrybox_IP;
	Label(root, text="IP(last 3 digits)").pack(fill=X);
	entrybox_IP = Entry(root);
	entrybox_IP.pack(fill=X);

def create_Parameter_Entrybox(root):
	global entrybox_Parameter;
	Label(root, text="Parameter").pack(fill=X);
	entrybox_Parameter = Entry(root);
	entrybox_Parameter.pack(fill=X);

def create_Value_Entrybox(root):
	global entrybox_Value;
	Label(root, text="Value").pack(fill=X);
	entrybox_Value = Entry(root);
	entrybox_Value.pack(fill=X);

def Send_data_continously():
	global data;	
	data = "192:168:0:" + entrybox_IP.get() + "," + entrybox_Parameter.get() + "," + entrybox_Value.get();
	while True:
		conn, addr = sock.accept();
		start_new_thread(clientthread_continously,(conn,)); 	
	
def clientthread_continously(conn):
	while True:
		conn.send(data + '\n'); 
		#conn.send('Is it working\n');  #for debugging			
		data_received = conn.recv(1024); # 1024 stands for bytes of data to be received
		print data_received;
	conn.close();
	sock.close();

def Send_data_once():
	global data;	
	#print mystring; 		#for debugging
	data = "192:168:0:" + entrybox_IP.get() + "," + entrybox_Parameter.get() + "," + entrybox_Value.get();
	while True:	
		conn, addr = sock.accept();
		start_new_thread(clientthread_once,(conn,)); 	
	print 'Connected by',addr;
	#conn.send('This is also working');    #for debugging
		
def clientthread_once(conn):
	#conn.send('This also worked but changed\n');
	conn.send(data + '\n');
	data_received = conn.recv(1024); 
	print data_received;
	conn.close();	
	sock.close();

def send_TOAllClients_once():
	global entrybox_IP;
	global data;
	if(entrybox_IP.get() == ""):
		showinfo("Message","Data will be send to all clients Once");
	else:
		showinfo("Message","An IP Address is selected");

	data = entrybox_Parameter.get() + "," + entrybox_Value.get();
	
	while True:
		conn, addr = sock.accept();
		start_new_thread(clientthread_to_all_once,(conn,)); 	
	print 'Connected by',addr;
	
def clientthread_to_all_once(conn):
	conn.send(data + '\n'); #send only takes string
	data_received = conn.recv(1024); # 1024 stands for bytes of data to be received
	print data_received;	
	conn.close();
	sock.close();
					
def send_TOAllClients_continously():
	global entrybox_IP;
	global data;
	if(entrybox_IP.get() == ""):
		showinfo("Message","Data will be send to all clients Continously");
	else:
		showinfo("Message","An IP Address is selected");
	
	data = entrybox_Parameter.get() + "," + entrybox_Value.get();
	
	while True:
		conn, addr = sock.accept();
		start_new_thread(clientthread_to_all_continously,(conn,)); 	
	
def clientthread_to_all_continously(conn):
	while True:
		conn.send(data + '\n'); #send only takes string
		data_received = conn.recv(1024); # 1024 stands for bytes of data to be received
		print data_received;
 	conn.close();
	sock.close();


def read():
	global output_file; 
	output_file=file(path,"a");
	while True:
		conn, addr = sock.accept();
		start_new_thread(clientthread_read,(conn,)); 	
	
def clientthread_read(conn):
	while True: 
		output_file=file(path,"a");
		data_received = conn.recv(1024); 
		print >> output_file,data_received;		
		time.sleep(0.001);		
		del output_file;
		
	conn.close();
	sock.close();				


def exit():
	root.quit();


root = Tk();
root.title('GUI Wireless Telemetry');
root.geometry('450x450+200+200');
path="/home/lakshay/Desktop/datafile_wifi.txt";
output_file=file(path,"a");

host = '';  #'localhost' or '127.0.0.1' or '' are all same
port = 52097;
sock = socket(AF_INET,SOCK_STREAM);
sock.bind((host, port));
sock.listen(2);

#create_Port(root);
create_IP_Entrybox(root);
create_Parameter_Entrybox(root);
create_Value_Entrybox(root);

#Button(root, text='Establish Connection', command=establish_connection).pack(fill=X);
Button(root, text='Send Once', command=Send_data_once).pack(fill=X,pady=15);
Button(root, text='Send Continously', command=Send_data_continously).pack(fill=X,pady=15);
Button(root, text='Send To All(Once)', command=send_TOAllClients_once).pack(fill=X,pady=15);
Button(root, text='Send To All(Continously)', command=send_TOAllClients_continously).pack(fill=X,pady=15);
Button(root, text='Read Data', command=read).pack(fill=X,pady=15);
Button(root, text='Exit', command=exit).pack(fill=X,padx=20);

mainloop();
