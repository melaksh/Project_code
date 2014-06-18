import socket
import gtk,pygtk
import serial
import string
import time
from thread import *
#import gobject


class Wireless():
	def __init__(self):
		self.IP = 0;
		self.Parameter = 0;
		self.Value = 0;
		self.path="/home/lakshay/Desktop/datafile.txt";
		self.output_file=file(path,"r");
		#gobject.threads_init();
		self.Setting();
	
	def Setting(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL);
		self.win.connect('destroy',self.destroy); 
		self.win.set_position(gtk.WIN_POS_CENTER_ALWAYS);		
		self.win.set_size_request(500,500);
		self.win.show();

		self.box1 = gtk.VBox();
		self.win.add(self.box1);
		self.box1.show();
		self.mystring = gtk.Entry();
		#self.mystring1 = self.mystring.get_text();
		self.box1.pack_start(self.mystring);

		self.button1 = gtk.Button("Establish Connection");
		self.box1.pack_start(self.button1);
		self.button1.show();	
		self.button1.connect('clicked',self.Establish_connection); 

		self.button2 = gtk.Button("Send and Receive Once");
		self.box1.pack_start(self.button2);
		self.button2.show();	
		self.button2.connect('clicked',self.send_once); 	
	
		self.button3 = gtk.Button("Send and Receive Continously");
		self.box1.pack_start(self.button3);
		self.button3.show();	
		self.button3.connect('clicked',self.send_continously); 						
		
		self.button4 = gtk.Button("Close Connection");
		self.box1.pack_start(self.button4);
		self.button4.show();	
		self.button4.connect('clicked',self.close_connection);

		self.button5 = gtk.Button("Read Data Only");
		self.box1.pack_start(self.button5);
		self.button5.show();	
		self.button5.connect('clicked',self.read);		 		
		self.win.show_all();

	def send_once(self,widget):
		self.data = self.mystring.get_text();
		self.host = '';  #'localhost' or '127.0.0.1' or '' are all same
		self.port = 52079;
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
		self.sock.bind((self.host, self.port));
		self.sock.listen(2);		
		while True:
			self.conn, self.addr = self.sock.accept();
			start_new_thread(self.clientthread_once(self.conn),(self.conn,));
		print 'connected by',self.addr;		 	
	
	def clientthread_once(conn):		
		self.conn.send('Is it working finally\n');		
		#self.conn.send(self.data); #send only takes string
		#self.receivedata = self.conn.recv(1024); # 1024 stands for bytes of data to be received
		#print "Server send",self.data;
		self.conn.close();
		#self.sock.close();


	def send_continously(self,widget):
		self.data = self.mystring.get_text();
		while True:
			self.conn, self.addr = sock.accept();
			#self.start_new_thread(self.clientthread_continously,(self.conn,)); 	
	
	def clientthread_continously(conn):
		while True:
			conn.send(self.data); 
			#self.receivedata = self.conn.recv(1024);
			#print "Server send",self.data;
		
		self.conn.close();
		self.sock.close();


	def read(self,widget):
		self.output_file=file(path,"r");
		while True:
			self.conn, self.addr = sock.accept();
			#self.start_new_thread(clientthread_read,(conn,)); 	
	
	def clientthread_read(conn):
		while True: 
			self.receivedata = self.conn.recv(1024); 
			self.output_file=file(path,"a");
			print >> self.output_file,self.receivedata;		
			del self.output_file;
		
		self.conn.close();
		self.sock.close();				


	def destroy(self,widget):
		print "You clicked Close.";
		gtk.main_quit();

	def close_connection(self,widget):
		self.conn.close();
		self.sock.close();
		

	def Establish_connection(self,widget):
		self.host = '';  #'localhost' or '127.0.0.1' or '' are all same
		self.port = 52075;
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
		self.sock.bind((self.host, self.port));
		self.sock.listen(2);
		
def main():
	gtk.main();

if __name__ =="__main__":
	#host = '';  #'localhost' or '127.0.0.1' or '' are all same
	#port = 52000;
	#sock = socket(AF_INET,SOCK_STREAM);
	#sock.bind((host, port));
	#sock.listen(2);
	window = Wireless();
	main();

