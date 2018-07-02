import socket
import sys
import threading
from thread import *
import datetime
import random
import requests
import os



host = ''
port = 8220
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)
#Variable for the number of connections
numbOfConn = 5
addressList=[]
clients=set()

##############################################################################
#small database of our bot
greetings = ['hola', 'hello', 'hi', 'hey']
questions = ['how are you', 'how are you doing']
responses = ['okay', 'i am fine']
database={
    
    'where' : {'ecseminar': 'go to  admin lobby, take the stairs at the left go to the second floor,then enter into autonomous exam section lobby,there you can find the ec seminar hall on the right side',
                'analoglab': 'go to  admin lobby, take the stairs at the right , go to the second floor,then take first right,there you can find the lab on your right side',
               'library':'enter the admin lobby in the ground floor at the left corner you can find the library ','office':'Enter the admin lobby go straight there you can find AB001 on your right side.enter AB001 there you will find the office'
               ,'scholarshipsection':'enter the admin lobby go straight there you can find scholarship section on your right side','chemistry lab':'enter the admin lobby go staright at the dead end you will find AB007 that is chemistry lab'
               ,'physicslab':'enter the admin lobby go staright at the dead end take right ,there you will find staircase,take that staircase go to first floor there at your right you will find AB110 that is physics lab',
               'referencesection':'enter the admin lobby take left staircase go to first floor there you can find reference section','liclab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB201 on your right side that is lic lab',
               'communicationlab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB202c on your right side that is communication lab',
               'basicelectronicslab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB202b on your right side that is basicelectronics lab',
               'eyantralab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB204 on your right side that is eyantra lab',
               'simulationlab':'enter the admin lobby take right staircase go to second floor take first right,go straight ,at the dead end there you can find CS201 that is simlab',
               'networkinglab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB206 on your right side that is networking lab',
               'echodroom':'from pot circle go straight enter the right entrance of the main buulding ,take a staircase ,go to first floor,take left and there you can find EC102 that is hod room',
               'staffrooms':'from pot circle go straight enter the right entrance of the main building ,take a staircase ,go to first floor,take left and there you can find EC104,EC105,EC106 these are staff rooms',
               'digitallibrary':'from pot circle go straight enter the right entrance of the main building, there you can find Digital library'
            
               },
       
   'guide' : {'ecseminar': 'go to  admin lobby, take the stairs at the left go to the second floor,then enter into autonomous exam section lobby,there you can find the ec seminar hall on the right side',
                'analoglab': 'go to  admin lobby, take the stairs at the right , go to the second floor,then take first right,there you can find the lab on your right side',
               'library':'enter the admin lobby in the ground floor at the left corner you can find the library ','office':'Enter the admin lobby go straight there you can find AB001 on your right side.enter AB001 there you will find the office'
               ,'scholarshipsection':'enter the admin lobby go straight there you can find scholarship section on your right side','chemistry lab':'enter the admin lobby go staright at the dead end you will find AB007 that is chemistry lab'
               ,'physicslab':'enter the admin lobby go staright at the dead end take right ,there you will find staircase,take that staircase go to first floor there at your right you will find AB110 that is physics lab',
               'referencesection':'enter the admin lobby take left staircase go to first floor there you can find reference section','liclab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB201 on your right side that is lic lab',
               'communicationlab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB202c on your right side that is communication lab',
               'basicelectronicslab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB202b on your right side that is basicelectronics lab',
               'eyantralab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB204 on your right side that is eyantra lab',
               'simulationlab':'enter the admin lobby take right staircase go to second floor take first right,go straight ,at the dead end there you can find CS201 that is simlab',
               'networkinglab':'enter the admin lobby take right staircase go to second floor take first right there you can find AB206 on your right side that is networking lab',
               'echodroom':'from pot circle go straight enter the right entrance of the main buulding ,take a staircase ,go to first floor,take left and there you can find EC102 that is hod room',
               'digitallibrary':'from pot circle go straight enter the right entrance of the main building, there you can find Digital library',
               'staffrooms':'from pot circle go straight enter the right entrance of the main building ,take a staircase ,go to first floor,take left and there you can find EC104,EC105,EC106 these are staff rooms'
               
            }
    }
     


print ("Listening for client . . .")
###############################################################################
#chatbot code here
def chatbot(data, data1,latel):
    latel2 = 0
    for data2 in data1:
        print(data)
        if data2 in database[data]:
            print(database[data][data2])
            #os.system("flite -t '"+ database[data] +"'")
            sclient(database[data][data2])
            latel2 = 1
            break
        
    if( latel2== 0) and (latel ==1):
        i=0;
        latel2 = 0;
        latel =0;
        d = True
        while d:
            for h in range(0,len(data1)):
                word = ''
                if h != len(data1)-1:
                    word += data1[i] + data1[i+1]
                else:
                    d = False
                if word in database[data]:
                    print(database[data][word])
                    #os.system("flite -t '"+ database[data] +"'")
                    sclient(database[data][word])
                    d = False
                    break
                i +=1    
    else:                
        if data in questions:
            random_response = random.choice(responses)
            print(random_response)
            #os.system("flite -t '"+ random_response +"'")
            sclient(random_response)
        elif data in greetings:
            random_greeting = random.choice(greetings)
            print(random_greeting)
            sclient(random_greeting)
            #os.system("flite -t '"+ random_greeting +"'")

        elif 'time' in data:
            now = datetime.datetime.now()
            time=str(now.hour)+str("hours")+str(now.minute)+str("minutes")
            print(time)
            #os.system("flite -t '"+ time+"'")
            sclient(time)
        elif 'date'in data:
            now = datetime.datetime.now()
            date=str("%s/%s/%s" % (now.month,now.day,now.year))
            print(date)
            #os.system("flite -t '"+date+"'")
            sclient(date)
        else:
            sclient("sorry please repeat")

         
    
###############################################################################
#Sending Reply to all clients
def sclient(mess):
    for c in clients:
        try:
            c.send(mess)
        except:
            c.close()
##############################################################################
#server code here
def clientthread(conn,addressList):
 while True:
    
    output = conn.recv(2048);
    if output.strip() == "disconnect":
            conn.close()
            sys.exit("Received disconnect message.  Shutting down.")
            conn.send("connection loss")
    elif output:
            print ("Message received from client:")
            data=str(output).lower()
            print (data)
            data1 = data.split(" ")
            print(data1)
            print("Reply from the server:")
            latel = 0;
            for string in data1:
                print(string)
                if string in database:
                    print(string)
                    latel =1;
                    chatbot(string, data1,latel)
                    break
                elif output:
                    chatbot(data,[],[])
                    break
    else:
         sclient("sorry please repeat..") 
  
while True:
#Accepting incoming connections
       conn, address = server_socket.accept()
       print ("Connected to client at ", address)
       clients.add(conn)
       #Creating new thread. Calling clientthread function for this function and passing conn as argument.
       start_new_thread(clientthread,(conn,addressList))
conn.close()
sock.close()   
