import requests 
from bs4 import BeautifulSoup 

import serial
import time

send='a'
  
def news(): 
    # the target we want to open     
    url='http://192.168.43.253/'
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The news are as follow :-\n") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     
  
        # l is the list which contains all the text i.e news  
        l=soup.find() 
        
        #print("\n\n")
        #print(type(l))
        #print("\n\n")
        #now we want to print only the text part of the anchor. 
        #find all the elements of a, i.e anchor 
        #print(soup.get_text())
        str=soup.get_text()
        return(str[6])
        #for i in range(len(str)):
         #   print(i)
          #  print(str[i])
    else: 
        print("Error")
        
    
while(True):
    if(news()=='k'):
    
        if(send=='a'):   # first time it will get off. IF on --> off if off --> on
            send='d'     #after that if on -->off if off-->on

        elif(send=='d'):
            send='a'
 
 
        print("Start")
        port="COM8" #This will be different for various devices and on windows it will probably be a COM port.
        bluetooth=serial.Serial(port,9600,timeout=1000)#Start communications with the bluetooth unit
        print(bluetooth.name)
        bluetooth.flush()
        print('flushed')
        bluetooth.write(send.encode())
        #   bluetooth.flushInput() #This gives the bluetooth a little kick
        #for i in range(5): #send 5 groups of data to the bluetooth
        #	print("Ping")
        #	bluetooth.write(b"BOOP ")#These need to be bytes not unicode, plus a number
        #	input_data=bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
        #	print(input_data.decode())#These are bytes coming in so a decode is needed
        #	time.sleep(0.5) #A pause between bursts
        bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
        print("Done")
        time.sleep(5)
        
