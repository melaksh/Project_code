import gtk,pygtk
import serial
import string
import time
import gobject


class Serial():
	def __init__(self):
		self.mystring = 0;
		self.mystring1 = 0;
		self.ser = serial.Serial('/dev/ttyAMA0',115200,timeout=1);
		self.path= path="/home/pi/Desktop/datafile.txt";
		self.output_file=file(path,"a");
		gobject.threads_init();
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
		self.mystring1 = self.mystring.get_text();
		self.box1.pack_start(self.mystring);

		self.button1 = gtk.Button("Send_Once");
		self.box1.pack_start(self.button1);
		self.button1.show();	
		self.button1.connect('clicked',self.send_once); 	
	
		self.button2 = gtk.Button("Send_Continously");
		self.box1.pack_start(self.button2);
		self.button2.show();	
		self.button2.connect('clicked',self.send_continously); 				
			
		self.button3 = gtk.Button("Start Communication");
		self.box1.pack_start(self.button3);
		self.button3.show();	
		self.button3.connect('clicked',self.start_communication); 		
		
		self.button4 = gtk.Button("Close Communication");
		self.box1.pack_start(self.button4);
		self.button4.show();	
		self.button4.connect('clicked',self.close_communication);

		self.button5 = gtk.Button("Read Data");
		self.box1.pack_start(self.button5);
		self.button5.show();	
		self.button5.connect('clicked',self.read);		 		
		self.win.show_all();

	def send_once(self,widget):
		#print str(self.mystring.get_text());		
		self.ser.write(str(self.mystring.get_text()) + '\n');
	
	def send_continously(self,widget):
		#print self.mystring.get_text();
		try:
			while 1:
				#print str(self.mystring.get_text());
				self.ser.write(str(self.mystring.get_text()) + '\n');
				self.ser.close();
				time.sleep(0.0001);
				self.ser.open();
			
		except serial.serialutil.SerialException:
			pass;

	def read(self,widget):
		#self.mystring = 3;
		#print self.mystring;
		try:
			while 1:
				self.output_file=file(path,"a");
				print >> self.output_file,self.ser.readline();		
				del self.output_file;
				self.ser.close();
				time.sleep(0.0001);
				self.ser.open();
			
		except serial.serialutil.SerialException:
			pass;

	def destroy(self,widget):
		print "You clicked Close.";
		gtk.main_quit();

	def close_communication(self,widget):
		#self.mystring = 4;
		#print self.mystring;
		if(self.ser.isOpen() == 1):
			self.ser.close();
			self.ser.open();
		else:
			self.ser.open();		
			time.sleep(0.0001);
			self.ser.close();
		
	def start_communication(self,widget):
		#self.mystring = 5;
		#print self.mystring;
		if(self.ser.isOpen() == 0):
			self.ser.open();

		else:
			self.ser.close();
			time.sleep(0.0001);
			self.ser.open();
		
def main():
	gtk.main();

if __name__ =="__main__":
	window = Serial();
	main();

