#!/usr/bin/python

import io
import serial
import string
import time
#from bitstring import BitStream,BitArray   #But this is for Python3
from ast import literal_eval

#rot13=string.maketrans(
#	"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
#	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

ser=serial.Serial('/dev/ttyAMA0',115200,timeout=0.01);
#ser.open();

try:
	#for i in range(1,25):
	while 1:
		#line = ser.readline();
		#time.sleep(0.0001);
		#line_last = str(line).split("\r\n")
		#line = ser.read(3);
		#time.sleep(0.1);
		#comparison = ser.readline();
		#if (
			#line >="1\r\n" and line <="160\r\n"
		#   ):
			#ser.write('3');
			#print line;
		#if all(line<="155\r\n"]):
			#ser.write('2');
			#print line;
		#if int(line_last[0]) >= 150:  #converting char-->line_last[0] into integer if line_last[0]='a' 
			#ser.write('2');		      #then int(__)=97 which is same as ord('a')=97      
	    		#print int(line_last[0]);
		#ser.write(string.translate(line,rot13));
		#ser.write(rot13);
		try:
			#ser.write(str(2514)+'\n');
			ser.write("251,758"+"\n");
			ser.close();
			time.sleep(0.1);
			ser.open();
		except:
			pass;
		#print line_last[0];
		#else:
			#ser.write('5');
			#print "Error";

		
except serial.serialutil.SerialException:
	pass;

#while 1:
	#ser.readline();


ser.close();

	