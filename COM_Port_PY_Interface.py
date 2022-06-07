# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:22:46 2022

@author: Akash Chandra Behera
"""

import serial
import sys
import pandas as p

t_int=10 #The time interval for which measurments
#Note the counter will store data for every second from t=0 to t=t_int


serialPort = serial.Serial(port = "COM8", baudrate=115200,
                           bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)

serialString = ""    #Hold data coming over UART

data={'Count':[]} #define dict 

df = p.DataFrame(data=data) #convert the dict to DataFrame

while(1):

    #Wait until there is data in the serial buffer
    if(serialPort.in_waiting > 0):

        #Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        #Print the contents of the serial data
        output=serialString.decode('Ascii')
        print(output)
        df.loc[len(df.index)] = [output]

       #After t_int seconds of collecting data, close the port and exit the program
        if ((df.shape[0]+1)>t_int):
            serialPort.close()
            #df.to_csv('data.csv') #This writes a new data file if there is no such file.
            df.to_csv('data.csv', mode='a', index=True, header=False) #This appends to an existing data file
            sys.exit()
            
            
'''
serialPort is the an assigned name for the Com port being handled (along with the handling settings)
serialPort.close() is necessary as otherwise the device will just keep sending data through the port 
resulting in 'Access denied'  
'''
            
            