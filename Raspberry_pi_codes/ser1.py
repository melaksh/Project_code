#!/usr/bin/python

import io
import serial
import string
import time

ser=serial.Serial('/dev/ttyAMA0',38400,timeout=1);
path= path="/home/pi/Desktop/datafile.txt";
output_file=file(path,"a");

try:
	#for i in range(1,25):
	while 1:
		line = ser.readline();
		time.sleep(0.0001);
		line_last = str(line).split(",");
		output_file=file(path,"a");
				    
		print int(line_last[0]);
		print >> output_file,line_last[0];
		print int(line_last[1]);
		print >> output_file,line_last[1];
		print int(line_last[2]);
		print >> output_file,line_last[2];
	
		del output_file;
		ser.close();
		time.sleep(0.001);
		ser.open();
except serial.serialutil.SerialException:
	pass;

#while 1:
	#ser.readline();


ser.close();










						# Written in ser.py

#import io
#import serial

#ser=serial.Serial('/dev/ttyAMA0',115200,timeout=2);
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser));

#f=open('datafile.txt','a');

#sio.write(unicode("hello\n"));
#sio.flush() ;
#print hello == unicode("hello\n");

#while 1: ser.write("h");

#try: hello = sio.readlines(); print hello;
#except serial.serialutil.SerialException: pass;

#try: hello = ser.readlines(); print hello; 
#except serial.serialutil.SerialException: pass;

#f.write(hello); 
#f.close();

#for i in range(0,25): ser.write(i); 
#if i>=40: break;


#print hello

#ser.close();

#dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
