
				#This is done using tkinter module not the gtk

from Tkinter import *
import serial
import string
import time

def send_once():
	print mystring.get();		
	#ser.write(str(mystring.get) + '\n');
	
def send_continously():
	#print mystring.get();
	#try:
	while 1:
		print mystring.get();
			#ser.write(str(mystring.get()) + '\n');
			#ser.close();
			#time.sleep(0.0001);
			#ser.open();
			
	#except serial.serialutil.SerialException:
		#pass;

def read():
	mystring1 = 3;
	print mystring1;
	#try:
		#while 1:
			#output_file=file(path,"a");
			#print >> output_file,ser.readline();		
			#del output_file;
			#ser.close();
			#time.sleep(0.0001);
			#ser.open();
			
	#except serial.serialutil.SerialException:
		#pass;

def close_communication():
	mystring1 = 4;
	print mystring1;
	#if(ser.isOpen() == 1):
	#	ser.close();
	#	ser.open();
	#else:
	#	ser.open();		
	#	time.sleep(0.0001);
	#	ser.close();
	
def start_communication():
	mystring1 = 5;
	print mystring1;
	#if(ser.isOpen() == 0):
	#	ser.open();

	#else:
	#	ser.close();
	#	time.sleep(0.0001);
	#	ser.open();



master = Tk();
#self.ser = serial.Serial('/dev/ttyAMA0',115200,timeout=1);
#self.path= path="/home/pi/Desktop/datafile.txt";
#self.output_file=file(path,"a");
Label(master,text="Enter").grid(row=0,column=0,pady=20);
mystring = Entry(master);
mystring.grid(row=0,column=1);

Button(master, text='Start Communication', command=start_communication).grid(row=3,pady=10,padx=10);
Button(master, text='Send Once', command=send_once).grid(row=4,column=0,pady=10,padx=10);
Button(master, text='Send Continously', command=send_continously).grid(row=5,column=0,pady=10,padx=10);
Button(master, text='Read', command=read).grid(row=6,column=0,pady=10,padx=10);
Button(master, text='Close Communication', command=close_communication).grid(row=7,column=0,pady=10,padx=10);
Button(master, text='Quit', command=master.quit).grid(row=8,column=0,pady=10,padx=10);
	
mainloop();
