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

ser=serial.Serial('/dev/ttyAMA0',38400,timeout=1);
#ser.open();
path= path="/home/pi/Desktop/datafile.txt";
output_file=file(path,"a");

try:
	#for i in range(1,25):
	while 1:
		line = ser.readline();
		time.sleep(0.0001);
		line_last = str(line).split("\r\n");
		output_file=file(path,"a");
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
		if int(line_last[0]) >= 150:  
		#converting char-line_last[0] into integer if line_last[0]='a' then int(__)=97 which is same as ord('a')=97 . 
			#ser.write('2');
			#output_file=file(path,"a"); Bec. now in else condition we again have to give as del op-_file is not defined then.		    
			print int(line_last[0]);
			print >> output_file,line_last[0];
		#ser.write(string.translate(line,rot13));
		#ser.write(rot13);
		#ser.write("Y");
		#print line_last[0];
		else:
			#ser.write('5');
			#print "Error";
			print("Error");
		del output_file;
		ser.close();
		time.sleep(0.001);
		ser.open();
except serial.serialutil.SerialException:
	pass;

#while 1:
	#ser.readline();


ser.close();

