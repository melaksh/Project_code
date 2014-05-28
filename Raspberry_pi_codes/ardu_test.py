#!/usr/bin/python

import io
import serial
import string
import time
#from bitstring import BitStream,BitArray   #But this is for Python3
from ast import literal_eval


ser=serial.Serial('/dev/ttyAMA0',115200,timeout=1);
#ser.open();
path= path="/home/pi/Desktop/datafile.txt";
output_file=file(path,"a");

try:
	ser.write("s");
	while 1:
		#ser.write("a");
		#time.sleep(0.0001);
		#ser.readline();
		#time.sleep(0.0001);
		#line_last = str(line).split("\r\n");
		output_file=file(path,"a");
		#if int(line_last[0]) >= 150:  
			#ser.write('2');
			#output_file=file(path,"a"); 		    
			#print int(line_last[0]);
			#print >> output_file,line_last[0];		
		#print line;
		print >> output_file,ser.readline();
		#print line_last[0];
		#else:
			#ser.write('5');
			#print "Error";
			#print("Error");
		del output_file;
		ser.close();
		time.sleep(0.0001);
		ser.open();
except serial.serialutil.SerialException:
	pass;

#while 1:
	#ser.readline();


ser.close();

