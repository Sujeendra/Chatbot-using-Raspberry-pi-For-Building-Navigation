import socket
import sys
import threading
from thread import *
import datetime
import random

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
x=set()



##############################################################################
#Database of our bot
greetings = ['hola', 'hello', 'hi', 'hey']
questions = ['how are you', 'how are you doing']
responses = ['okay', 'i am fine']
database={
    
'g1' : {'d1':'Take right staircase go to second floor and take the first right, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab ',
	'd2':'Take right staircase go to second floor and take the first right, there you can find AB206 to your right side which is the CISCO lab',
	'd2':'Take right staircase go to second floor and take the first right, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	'd4':'Take right staircase go to second floor and take the first right, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Take right staircase go to second floor and take the first right, there you can find AB203 to your right side which is the PG classroom',
	'd6':'Take right staircase go to second floor and take the first right, there you can find AB202c to your right side that is Communication lab',
	'd7':'Take right staircase go to second floor and take the first right, there you can find AB202b to your right side which is the Digital Electronics lab',
        'd8':'Take right staircase go to second floor and take the first right, there you can find AB202a',
	'd9':'Take the stairs at the right , go to the second floor,then take first right,there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	'd10':'Take the stairs at the left go to the second floor,then enter into autonomous exam section lobby,there you can find the EC Seminar Hall on the right side',
        'd11':'Take the staircase to the left go to second floor take first left, there you can find CS201 to the left that is Networking/Simulation lab',
	'd12':'Take the staircase to the left go to second floor take first left, there you can find CS202 to the left that is Automotive & Control lab',
        'd13':'Take the staircase to the left go to second floor take first left, there you can find CS203 to the left that is Power Electronics Lab',
	'd14':'Take the staircase to the left go to second floor take first left, there you can find Autonomous Exam Section at the dead end',
	'd15':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC106 to your right',
	'd17':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC105 to your right',
	'd18':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Enter the admin lobby take left staircase go to first floor there you can find Reference Section',
	'd22':'Take right staircase go to first floor and take the first right, there you can find AB101 which is the PG Section',
	'd23':'Take right staircase go to first floor and take the first right, there you can find AB102 which is the PG Class',
	'd24':'Take right staircase go to first floor and take the first right, there you can find AB103',
	'd25':'Take right staircase go to first floor and take the first right, there you can find AB104 which is the EC Class',
	'd26':'Take right staircase go to first floor and take the first right, there you can find AB105',
	'd27':'Take right staircase go to first floor and take the first right, there you can find AB106 which is the PG Class',
	'd28':'Take right staircase go to first floor and take the first right, there you can find AB107 which is the PG Lecture Hall',
	'd29':'Take right staircase go to first floor and take the first right, there you can find AB108',
	'd30':'Take right staircase go to first floor and take the first right, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Take right staircase go to first floor and take the first right, and go to the dead end, there you can find AB110 which is the Physics Lab',
	'd32':'Take right staircase go to first floor and take the first right, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	'd33':'Go straight, at the dead end you will find AB007 that is Dept. of Chemistry/Lab',
	'd34':'Go straight, there you can find Toilet to your right side',
	'd35':'Go straight, there you can find UPS room to your right side',
	'd36':'Go straight, there you can find Alumni assosiation to your right side',
	'd37':'Go straight, there you can find Registror's office to your right side',
	'd38':'Go straight, there you can find Principal's office to your right side',
	'd39':'Go straight, there you can find Office to your right side',
	'd40':'You can find the Library to the left'  
               },
       
'g2' : {'d1':'Take the staircase go to second floor and you will find DSP & Image Processing/VLSI/Microcontroller Lab to your right',
	'd2':'Take the staircase go to second floor and go left and you find AB206 to your left side which is the CISCO lab',
	'd2':'Take the staircase go to second floor and go left and you find AB205 to your left side which is the Calibration & Servicing Center',
	'd4':'Take the staircase go to second floor and go left and you find AB204 to your left side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Take the staircase go to second floor and go left and you find AB203 to your left side which is the PG classroom',
	'd6':'Take the staircase go to second floor and go left and you find AB202c to your laft side that is Communication lab',
	'd7':'Take the staircase go to second floor and go left and you find AB202b to your left side which is the Digital Electronics lab',
        'd8':'Take the staircase go to second floor and go left and you find AB202a to your left side',
	'd9':'Take the staircase go to second floor and go left and you find EC201 to your right at the end of the corridor which is the Analog/LIC lab on your right side',
	'd10':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find the EC Seminar Hall on the right side',
        'd11':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find CS201 to the left that is Networking/Simulation lab',
	'd12':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find CS202 to the left that is Automotive & Control lab',
        'd13':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find CS203 to the left that is Power Electronics Lab',
	'd14':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find Autonomous Exam Section at the dead end',
	'd15':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC106 to your right',
	'd17':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC105 to your right',
	'd18':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Take the staircase go to first floor and go left till the lobby, there you can find Reference Section',
	'd22':'Take the staircase go to first floor and go left, there you can find on your left side AB101 which is the PG Section',
	'd23':'Take the staircase go to first floor and take left, there you can find AB102 which is the PG Class',
	'd24':'Take the staircase go to first floor and take left, there you can find AB103',
	'd25':'Take the staircase go to first floor and take left, there you can find AB104 which is the EC Class',
	'd26':'Take the staircase go to first floor and take left, there you can find AB105',
	'd27':'Take the staircase go to first floor and take left, there you can find AB106 which is the PG Class',
	'd28':'Take the staircase go to first floor and take left, there you can find AB107 which is the PG Lecture Hall',
	'd29':'Take the staircase go to first floor and take left, there you can find AB108',
	'd30':'Take the staircase go to first floor and take left, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Take the staircase go to first floor and take left, there you can find AB110 which is the Physics Lab',
	'd32':'Take the staircase go to first floor where you can find on your right AB111 which is the Dept. of Physics/Lab',
	'd33':'You are here',
	'd34':'Go straight in corridor, there you can find Toilet to your left side',
	'd35':'Go straight in corridor, there you can find UPS room to your left side',
	'd36':'Go straight in corridor, there you can find Alumni assosiation to your left side',
	'd37':'Go straight in corridor, there you can find Registror's office to your left side',
	'd38':'Go straight in corridor, there you can find Principal's office to your left side',
	'd39':'Go straight in corridor, there you can find Office to your left side',
	'd40':'Go straight in corridor,enter the looby and you find Library to the right'
               },
'g3' : {'d1':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor at the end you will find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab ',
	'd2':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB206 to your right side which is the CISCO lab',
	'd2':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	'd4':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB203 to your right side which is the PG classroom',
	'd6':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB202c to your right side that is Communication lab',
	'd7':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB202b to your right side which is the Digital Electronics lab',
        'd8':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find AB202a',
	'd9':'Take the staircase go to second floor and take right, go till the lobby and enter the opposite corridor, there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	'd10':'Take the staircase go to second floor and take right,there you can find the EC Seminar Hall on the left side',
        'd11':'Take the staircase go to second floor and take right, there you can find CS201 to the right that is Networking/Simulation lab',
	'd12':'Take the staircase go to second floor and take right, there you can find CS202 to the right that is Automotive & Control lab',
        'd13':'Take the staircase go to second floor and take right, there you can find CS203 to the right that is Power Electronics Lab',
	'd14':'Take the staircase go to second floor, there you can find Autonomous Exam Section',
	'd15':'Take the staircase to the left and go to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Take the staircase to the left and go to the first floor and take left, there you can find EC106 to your right',
	'd17':'Take the staircase to the left and go to the first floor and take left, there you can find EC105 to your right',
	'd18':'Take the staircase to the left and go to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Take the staircase to the left and go to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Take the staircase to the left and go to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor there you can find Reference Section',
	'd22':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB101 which is the PG Section',
	'd23':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB102 which is the PG Class',
	'd24':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB103',
	'd25':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB104 which is the EC Class',
	'd26':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB105',
	'd27':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB106 which is the PG Class',
	'd28':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB107 which is the PG Lecture Hall',
	'd29':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB108',
	'd30':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, there you can find AB110 which is the Physics Lab',
	'd32':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to first floor go straight to corridor, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	'd33':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, you will find AB007 that is Dept. of Chemistry/Lab to your right',
	'd34':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor, there you can find Toilet to your left side',
	'd35':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor, there you can find UPS room to your left side',
	'd36':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor, there you can find Alumni assosiation to your left side',
	'd37':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor, there you can find Registror's office to your left side',
	'd38':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor, there you can find Principal's office to your left side',
	'd39':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor, there you can find Office to your right side',
	'd40':'Take the staircase go to second floor and take right, go till the lobby and take stairs to go to ground floor, go straight to corridor till the lobby, you can find the Library to the left'
               },
'g4' : { 'd1':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab',
         'd2':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB206 to your right side which is the CISCO lab',
	 'd3':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	 'd4':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	 'd5':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB203 to your right side which is the PG classroom',
	 'd6':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB202c to your right side that is Communication lab',
	 'd7':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB202b to your right side which is the Digital Electronics lab',
	 'd8':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB202a',
	 'd9':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	 'd10':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find the EC Seminar Hall on the left side',
	 'd11':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find CS201 to the right that is Networking/Simulation lab',
	 'd12':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find CS202 to the right that is Automotive & Control lab',
	 'd13':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find CS203 to the right that is Power Electronics Lab',
	 'd14':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find Autonomous Exam Section to the left',
	 'd15':'Take the stairs to your left to the first floor, then take left to enter the passage, there you can find EC101 to your right which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	 'd16':'Take the stairs to your left to the first floor, then take left to enter the passage, there you can find EC106 to your left in the passage', 
	 'd17':'Take the stairs to your left to the first floor, then take left to enter the passage, there you can find EC105 to your left in the passage',
	 'd18':'Take the stairs to your left to the first floor, then take left to enter the passage, there you can find EC104 to your left which is the Staff Rooms(Female) in the passage',
	 'd19':'Take the stairs to your left to the first floor, there you can find the EC HOD room',
	 'd20':'Take the stairs to your left to the first floor, there you can find EC103, which is the Ladies Toilet',
	 'd21':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the first floor, there you can find the Reference Section',
	 'd22':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, there you can find AB101 which is the PG Section',
	 'd32':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	 'd33':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, at the dead end you will find AB007 which is the Dept. of Chemistry/Lab',
	 'd34':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Toilet to your right side',
	 'd35':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find UPS room to your right side',
	 'd36':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Alumni assosiation to your right side',
	 'd37':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Registror's office to your right side',
	 'd38':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Principal's office to your right side',
	 'd39':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, there you can find Office to your right side',
	 'd40':'Take the stairs to your left to the first floor, then go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the ground floor, there you can find the Library to the left'
               },
'f1' : {'d1':'Take right staircase go to second floor and take the first right, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab ',
	'd2':'Take right staircase go to second floor and take the first right, there you can find AB206 to your right side which is the CISCO lab',
	'd2':'Take right staircase go to second floor and take the first right, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	'd4':'Take right staircase go to second floor and take the first right, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Take right staircase go to second floor and take the first right, there you can find AB203 to your right side which is the PG classroom',
	'd6':'Take right staircase go to second floor and take the first right, there you can find AB202c to your right side that is Communication lab',
	'd7':'Take right staircase go to second floor and take the first right, there you can find AB202b to your right side which is the Digital Electronics lab',
        'd8':'Take right staircase go to second floor and take the first right, there you can find AB202a',
	'd9':'Take the stairs at the right , go to the second floor,then take first right,there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	'd10':'Take the stairs at the left go to the second floor,then enter into autonomous exam section lobby,there you can find the EC Seminar Hall on the right side',
        'd11':'Take the staircase to the left go to second floor take first left, there you can find CS201 to the left that is Networking/Simulation lab',
	'd12':'Take the staircase to the left go to second floor take first left, there you can find CS202 to the left that is Automotive & Control lab',
        'd13':'Take the staircase to the left go to second floor take first left, there you can find CS203 to the left that is Power Electronics Lab',
	'd14':'Take the staircase to the left go to second floor take first left, there you can find Autonomous Exam Section at the dead end',
	'd15':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC106 to your right',
	'd17':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC105 to your right',
	'd18':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Take the staircase to the left and go to the second floor and take the first left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Enter the admin lobby take left staircase go to first floor there you can find Reference Section',
	'd22':'Go straight in corridor, there you can find AB101 which is the PG Section',
	'd23':'Go straight in corridor, there you can find AB102 which is the PG Class',
	'd24':'Go straight in corridor, there you can find AB103',
	'd25':'Go straight in corridor, there you can find AB104 which is the EC Class',
	'd26':'Go straight in corridor, there you can find AB105',
	'd27':'Go straight in corridor, there you can find AB106 which is the PG Class',
	'd28':'Go straight in corridor, there you can find AB107 which is the PG Lecture Hall',                                                     
	'd29':'Go straight in corridor, there you can find AB108',
	'd30':'Go straight in corridor, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Go straight in corridor, there you can find AB110 which is the Physics Lab',
	'd32':'Go straight in corridor, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	'd33':'Take right staircase go to ground floor and take the first right, at the dead end you will find AB007 that is Dept. of Chemistry/Lab',
	'd34':'Take right staircase go to ground floor and take the first right, there you can find Toilet to your right side',
	'd35':'Take right staircase go to ground floor and take the first right, there you can find UPS room to your right side',
	'd36':'Take right staircase go to ground floor and take the first right, there you can find Alumni assosiation to your right side',
	'd37':'Take right staircase go to ground floor and take the first right, there you can find Registror's office to your right side',
	'd38':'Take right staircase go to ground floor and take the first right, there you can find Principal's office to your right side',
	'd39':'Take right staircase go to ground floor and take the first right, there you can find Office to your right side',
	'd40':'Take right staircase go to ground floor and take the first right, you can find the Library in front'
               },
'f2' : {'d1':'Take the staircase go to second floor and you will find DSP & Image Processing/VLSI/Microcontroller Lab to your right',
	'd2':'Take the staircase go to second floor and go left and you find AB206 to your left side which is the CISCO lab',
	'd2':'Take the staircase go to second floor and go left and you find AB205 to your left side which is the Calibration & Servicing Center',
	'd4':'Take the staircase go to second floor and go left and you find AB204 to your left side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Take the staircase go to second floor and go left and you find AB203 to your left side which is the PG classroom',
	'd6':'Take the staircase go to second floor and go left and you find AB202c to your laft side that is Communication lab',
	'd7':'Take the staircase go to second floor and go left and you find AB202b to your left side which is the Digital Electronics lab',
        'd8':'Take the staircase go to second floor and go left and you find AB202a to your left side',
	'd9':'Take the staircase go to second floor and go left and you find EC201 to your right at the end of the corridor which is the Analog/LIC lab on your right side',
	'd10':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find the EC Seminar Hall on the right side',
        'd11':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find CS201 to the left that is Networking/Simulation lab',
	'd12':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find CS202 to the left that is Automotive & Control lab',
        'd13':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find CS203 to the left that is Power Electronics Lab',
	'd14':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, there you can find Autonomous Exam Section at the dead end',
	'd15':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC106 to your right',
	'd17':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC105 to your right',
	'd18':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Take the staircase go to second floor and go left till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Go straight in corridor till the lobby, there you can find Reference Section',
	'd22':'Go straight in corridor, there you can find on your left side AB101 which is the PG Section',
	'd23':'Go straight in corridor, there you can find AB102 which is the PG Class',
	'd24':'Go straight in corridor, there you can find AB103',
	'd25':'Go straight in corridor, there you can find AB104 which is the EC Class',
	'd26':'Go straight in corridor, there you can find AB105',
	'd27':'Go straight in corridor, there you can find AB106 which is the PG Class',
	'd28':'Go straight in corridor, there you can find AB107 which is the PG Lecture Hall',
	'd29':'Go straight in corridor, there you can find AB108',
	'd30':'Go straight in corridor, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Go straight in corridor, there you can find AB110 which is the Physics Lab',
	'd32':'You are here',
	'd33':'Take the staircase go to ground floor where you can find on your right AB111 which is the Dept. of Chemistry/Lab',
	'd34':'Take the staircase go to ground floor, Go straight in corridor, there you can find Toilet to your left side',
	'd35':'Take the staircase go to ground floor, Go straight in corridor, there you can find UPS room to your left side',
	'd36':'Take the staircase go to ground floor, Go straight in corridor, there you can find Alumni assosiation to your left side',
	'd37':'Take the staircase go to ground floor, Go straight in corridor, there you can find Registror's office to your left side',
	'd38':'Take the staircase go to ground floor, Go straight in corridor, there you can find Principal's office to your left side',
	'd39':'Take the staircase go to ground floor, Go straight in corridor, there you can find Office to your left side',
	'd40':'Take the staircase go to ground floor, Go straight in corridor,enter the looby and you find Library to the right'
               },
'f3' : { 'd1':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab',
         'd2':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB206 to your right side which is the CISCO lab',
	 'd3':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	 'd4':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	 'd5':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB203 to your right side which is the PG classroom',
	 'd6':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB202c to your right side that is Communication lab',
	 'd7':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB202b to your right side which is the Digital Electronics lab',
	 'd8':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find AB202a',
	 'd9':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end and then take left, take left again, there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	 'd10':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find the EC Seminar Hall on the left side',
	 'd11':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find CS201 to the right that is Networking/Simulation lab',
	 'd12':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find CS202 to the right that is Automotive & Control lab',
	 'd13':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find CS203 to the right that is Power Electronics Lab',
	 'd14':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right, there you can find Autonomous Exam Section to the left',
	 'd15':'You can find EC101 to your right which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	 'd16':'You can find EC106 to your left in the passage', 
	 'd17':'You can find EC105 to your left in the passage',
	 'd18':'You can find EC104 to your left which is the Staff Rooms(Female) in the passage',
	 'd19':'You are infront of EC HOD room',
	 'd20':'You can find EC103 behind, which is the Ladies Toilet',
	 'd21':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the first floor, there you can find the Reference Section',
	 'd22':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, there you can find AB101 which is the PG Section',
	 'd23':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB102 which is the PG Class',
	 'd24':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB103',
	 'd25':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB104 which is the EC Class',
	 'd26':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB105',
	 'd27':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB106 which is the PG Class',
	 'd28':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB107 which is the PG Lecture Hall',                                                     
	 'd29':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB108',
	 'd30':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB109 which is the Chemistry research Lab',
	 'd31':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB110 which is the Physics Lab',
	 'd32':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	 'd33':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, at the dead end you will find AB007 which is the Dept. of Chemistry/Lab',
	 'd34':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Toilet to your right side',
	 'd35':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find UPS room to your right side',
	 'd36':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Alumni assosiation to your right side',
	 'd37':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Registror's office to your right side',
	 'd38':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Principal's office to your right side',	 	 
	 'd39':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, there you can find Office to your right side',
	 'd40':'Go straight to the end of the passage and take the stairs on your right to the second floor, take right and go to the end, then take stairs to your left to the ground floor, there you can find the Library to the left'
	    },
'f4' : { 'd1':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab',
         'd2':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB206 to your right side which is the CISCO lab',
	 'd3':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	 'd4':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	 'd5':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB203 to your right side which is the PG classroom',
	 'd6':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB202c to your right side that is Communication lab',
	 'd7':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB202b to your right side which is the Digital Electronics lab',
	 'd8':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find AB202a',
	 'd9':'Take the stairs to the second floor, take right and go to the end and then take left, take left again, there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	 'd10':'Take the stairs to the second floor, take right, there you can find the EC Seminar Hall on the left side',
	 'd11':'Take the stairs to the second floor, take right, there you can find CS201 to the right that is Networking/Simulation lab',
	 'd12':'Take the stairs to the second floor, take right, there you can find CS202 to the right that is Automotive & Control lab',
	 'd13':'Take the stairs to the second floor, take right, there you can find CS203 to the right that is Power Electronics Lab',
	 'd14':'Take the stairs to the second floor, take right, there you can find Autonomous Exam Section to the left',
	 'd15':'You can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	 'd16':'You are infront of EC106', 
	 'd17':'Enter the passage and you can find EC105 to your right',
	 'd18':'Enter the passage and you can find EC104 to your right which is the Staff Rooms(Female) in the passage',
	 'd19':'Enter the passage and you can find EC HOD room to your left',
	 'd20':'Enter the passage and you can find EC103 to your left, which is the Ladies Toilet',
	 'd21':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the first floor, there you can find the Reference Section',
	 'd22':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, there you can find AB101 which is the PG Section',
	 'd23':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB102 which is the PG Class',
	 'd24':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB103',
	 'd25':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB104 which is the EC Class',
	 'd26':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB105',
	 'd27':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB106 which is the PG Class',
	 'd28':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB107 which is the PG Lecture Hall',                                                     
	 'd29':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB108',
	 'd30':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB109 which is the Chemistry research Lab',
	 'd31':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB110 which is the Physics Lab',	 
	 'd32':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the first floor, take the first right, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	 'd33':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, at the dead end you will find AB007 which is the Dept. of Chemistry/Lab',
	 'd34':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Toilet to your right side',
	 'd35':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find UPS room to your right side',
	 'd36':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Alumni assosiation to your right side',
	 'd37':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Registror's office to your right side',
	 'd38':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Principal's office to your right side',	 	 
	 'd39':'Take the stairs to the second floor, take right and go to the end, then take stairs to your right to the ground floor and then take right, go straight, there you can find Office to your right side',
	 'd40':'Take the stairs to the second floor, take right and go to the end, then take stairs to your left to the ground floor, there you can find the Library to the left'
               },
's1' : {'d1':'Take the passage to your right, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab ',
	'd2':'Take the passage to your right, there you can find AB206 to your right side which is the CISCO lab',
	'd3':'Take the passage to your right, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	'd4':'Take the passage to your right, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Take the passage to your right, there you can find AB203 to your right side which is the PG classroom',
	'd6':'Take the passage to your right, there you can find AB202c to your right side that is Communication lab',
	'd7':'Take the passage to your right, there you can find AB202b to your right side which is the Digital Electronics lab',
        'd8':'Take the passage to your right, there you can find AB202a',
	'd9':'Take the passage to your right, there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	'd10':'Enter into the Autonomous exam section lobby to your left, there you can find the EC Seminar Hall on the right side',
        'd11':'Enter into the Autonomous exam section lobby to your left, there you can find CS201 to the left that is Networking/Simulation lab',
	'd12':'Enter into the Autonomous exam section lobby to your left, there you can find CS202 to the left that is Automotive & Control lab',
        'd13':'Enter into the Autonomous exam section lobby to your left, there you can find CS203 to the left that is Power Electronics Lab',
	'd14':'Enter into the Autonomous exam section lobby to your left, there you can find Autonomous Exam Section at the dead end',
	'd15':'Enter into the Autonomous exam section lobby to your left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Enter into the Autonomous exam section lobby to your left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC106 to your right',
	'd17':'Enter into the Autonomous exam section lobby to your left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC105 to your right',
	'd18':'Enter into the Autonomous exam section lobby to your left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Enter into the Autonomous exam section lobby to your left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Enter into the Autonomous exam section lobby to your left, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Take the staircase to your left to go to the first floor, there you can find the Reference Section',
	'd22':'Take staircase to your right and go to first floor and take the first right, there you can find AB101 which is the PG Section',
	'd23':'Take right staircase go to first floor and take the first right, there you can find AB102 which is the PG Class',
	'd24':'Take right staircase go to first floor and take the first right, there you can find AB103',
	'd25':'Take right staircase go to first floor and take the first right, there you can find AB104 which is the EC Class',
	'd26':'Take right staircase go to first floor and take the first right, there you can find AB105',
	'd27':'Take right staircase go to first floor and take the first right, there you can find AB106 which is the PG Class',
	'd28':'Take right staircase go to first floor and take the first right, there you can find AB107 which is the PG Lecture Hall',
	'd29':'Take right staircase go to first floor and take the first right, there you can find AB108',
	'd30':'Take right staircase go to first floor and take the first right, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Take right staircase go to first floor and take the first right, and go to the dead end, there you can find AB110 which is the Physics Lab',
	'd32':'Take staircase to your right and go to first floor and take the first right, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	'd33':'Take staircase to your right and go to first floor and take the first right, Go straight, at the dead end you will find AB007 which is the Dept. of Chemistry/Lab',
	'd34':'Take right staircase go to ground floor and take the first right, there you can find Toilet to your right side',
	'd35':'Take right staircase go to ground floor and take the first right, there you can find UPS room to your right side',
	'd36':'Take right staircase go to ground floor and take the first right, there you can find Alumni assosiation to your right side',
	'd37':'Take right staircase go to ground floor and take the first right, there you can find Registror's office to your right side',
	'd38':'Take right staircase go to ground floor and take the first right, there you can find Principal's office to your right side',	
	'd39':'Take staircase to your right and go to first floor and take the first right, Go straight, there you can find Office to your right side',
	'd40':'Take the staircase to your left to go to the ground floor, there you can find the Library to the left'
               },
's2' : {'d1':'You are here',
	'd2':'Go straight in corridor and you find AB206 to your left side which is the CISCO lab',
	'd2':'Go straight in corridor and you find AB205 to your left side which is the Calibration & Servicing Center',
	'd4':'Go straight in corridor and you find AB204 to your left side which is the Robotics/Embedded Systems/E-Yantra lab',
	'd5':'Go straight in corridor and you find AB203 to your left side which is the PG classroom',
	'd6':'Go straight in corridor and you find AB202c to your laft side that is Communication lab',
	'd7':'Go straight in corridor and you find AB202b to your left side which is the Digital Electronics lab',
        'd8':'Go straight in corridor and you find AB202a to your left side',
	'd9':'Go straight in corridor and you find EC201 to your right at the end of the corridor which is the Analog/LIC lab on your right side',
	'd10':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, there you can find the EC Seminar Hall on the right side',
        'd11':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, there you can find CS201 to the left that is Networking/Simulation lab',
	'd12':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, there you can find CS202 to the left that is Automotive & Control lab',
        'd13':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, there you can find CS203 to the left that is Power Electronics Lab',
	'd14':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, there you can find Autonomous Exam Section at the dead end',
	'd15':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	'd16':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC106 to your right',
	'd17':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC105 to your right',
	'd18':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC104 to your right which is the Staff Rooms(Female)',
	'd19':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC102 to your left which is the EC HOD room',
	'd20':'Go straight in corridor till the lobby,then enter into autonomous exam section lobby, Go till the Autonomous section, take the Staircase to the left to the first floor and take left, there you can find EC103 to your left which is the Ladies Toilet',
	'd21':'Go straight in corridor till the lobby, there you can find Reference Section',
	'd22':'Take the staircase go to first floor and go left, there you can find on your left side AB101 which is the PG Section',
	'd23':'Take the staircase go to first floor and take left, there you can find AB102 which is the PG Class',
	'd24':'Take the staircase go to first floor and take left, there you can find AB103',
	'd25':'Take the staircase go to first floor and take left, there you can find AB104 which is the EC Class',
	'd26':'Take the staircase go to first floor and take left, there you can find AB105',
	'd27':'Take the staircase go to first floor and take left, there you can find AB106 which is the PG Class',
	'd28':'Take the staircase go to first floor and take left, there you can find AB107 which is the PG Lecture Hall',
	'd29':'Take the staircase go to first floor and take left, there you can find AB108',
	'd30':'Take the staircase go to first floor and take left, there you can find AB109 which is the Chemistry research Lab',
	'd31':'Take the staircase go to first floor and take left, there you can find AB110 which is the Physics Lab',
	'd32':'Take the staircase go to first floor where you can find on your right AB111 which is the Dept. of Physics/Lab',
	'd33':'Take the staircase go to ground floor where you can find on your right AB111 which is the Dept. of Chemistry/Lab',
	'd34':'Take the staircase go to ground floor, Go straight in corridor, there you can find Toilet to your left side',
	'd35':'Take the staircase go to ground floor, Go straight in corridor, there you can find UPS room to your left side',
	'd36':'Take the staircase go to ground floor, Go straight in corridor, there you can find Alumni assosiation to your left side',
	'd37':'Take the staircase go to ground floor, Go straight in corridor, there you can find Registror's office to your left side',
	'd38':'Take the staircase go to ground floor, Go straight in corridor, there you can find Principal's office to your left side',
	'd39':'Take the staircase go to ground floor, Go straight in corridor, there you can find Office to your left side',
	'd40':'Take the staircase go to ground floor, Go straight in corridor,enter the looby and you find Library to the right'
               },
's3' : { 'd1':'Go to the end of the lobby and then take left, take left again, go to the end of the lab to find AB208 which is DSP & Image Processing/VLSI/Microcontroller Lab',
         'd2':'Go to the end of the lobby and then take left, take left again, there you can find AB206 to your right side which is the CISCO lab',
	 'd3':'Go to the end of the lobby and then take left, take left again, there you can find AB205 to your right side which is the Calibration & Servicing Center',
	 'd4':'Go to the end of the lobby and then take left, take left again, there you can find AB204 to your right side which is the Robotics/Embedded Systems/E-Yantra lab',
	 'd5':'Go to the end of the lobby and then take left, take left again, there you can find AB203 to your right side which is the PG classroom',
	 'd6':'Go to the end of the lobby and then take left, take left again, there you can find AB202c to your right side that is Communication lab',
	 'd7':'Go to the end of the lobby and then take left, take left again, there you can find AB202b to your right side which is the Digital Electronics lab',
	 'd8':'Go to the end of the lobby and then take left, take left again, there you can find AB202a',
	 'd9':'Go to the end of the lobby and then take left, take left again, there you can find EC201 to your right which is the Analog/LIC lab on your right side',
	 'd10':'Enter the lobby, there you can find the EC Seminar Hall on the left side',
	 'd11':'Enter the lobby, there you can find CS201 to the right that is Networking/Simulation lab',
	 'd12':'Enter the lobby, there you can find CS202 to the right that is Automotive & Control lab',
	 'd13':'Enter the lobby, there you can find CS203 to the right that is Power Electronics Lab',
	 'd14':'You are infront of the Autonomous Exam Section',
	 'd15':'Take the stairs to the first floor, and take left, there you can find EC101 to your left which is the EC dept library/Nano Dielectric Devices Reasearch Lab',
	 'd16':'Take the stairs to the first floor and take left, there you can find EC106 to your right', 
	 'd17':'Take the stairs to the first floor, and take left to enter the passage and you can find EC105 to your right',
	 'd18':'Take the stairs to the first floor, and take left to enter the passage and you can find EC104 to your right which is the Staff Rooms(Female) in the passage',
	 'd19':'Take the stairs to the first floor, and take left to enter the passage and you can find EC HOD room to your left',
	 'd20':'Take the stairs to the first floor, and take left to enter the passage and you can find EC103 to your left, which is the Ladies Toilet',
	 'd21':'Go to the end of the lobby, then take stairs to your right to the first floor, there you can find the Reference Section',
	 'd22':'Go to the end of the lobby, then take stairs to your left to the first floor, take the first right, there you can find AB101 which is the PG Section',
	 'd23':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB102 which is the PG Class',
	 'd24':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB103',
	 'd25':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB104 which is the EC Class',
	 'd26':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB105',
	 'd27':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB106 which is the PG Class',
	 'd28':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB107 which is the PG Lecture Hall',                                                     
	 'd29':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB108',
	 'd30':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB109 which is the Chemistry research Lab',
	 'd31':'Go to the end, then take stairs to your left to the first floor, take the first right, Go straight in corridor, there you can find AB110 which is the Physics Lab',	 
	 'd32':'Go to the end of the lobby, then take stairs to your left to the first floor, take the first right, go to the dead end where you can find AB111 which is the Dept. of Physics/Lab',
	 'd33':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, at the dead end you will find AB007 which is the Dept. of Chemistry/Lab',
	 'd34':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Toilet to your right side',
	 'd35':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find UPS room to your right side',
	 'd36':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Alumni assosiation to your right side',
	 'd37':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Registror's office to your right side',
	 'd38':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, Go straight, there you can find Principal's office to your right side',	 	 
	 'd39':'Go to the end of the lobby, then take stairs to your right to the ground floor and then take right, go straight, there you can find Office to your right side',
	 'd40':'Go to the end of the lobby, then take stairs to your left to the ground floor, there you can find the Library to the left'
               },

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
        

         
    
###############################################################################
#Sending Reply to all clients
def sclient(mess):
    
    for c in clients:
        print x
        try:
            for i in x:
              if i==c:
                
                 c.send(mess)
                 x.remove(i)
            else:
                continue
        except:
           
            c.close()
##############################################################################
#server code here
def clientthread(conn,addressList):

 while True:

    
    output =conn.recv(2048)
    for c in clients:
        if conn==c:
            x.add(c)
            
    
    if output== "disconnect":
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
       
       
       print ("Connected to client at ", str(address))
       clients.add(conn)
       addressList.append(str(address))
       #Creating new thread. Calling clientthread function for this function and passing conn as argument.
       start_new_thread(clientthread,(conn,addressList))
conn.close()
sock.close() 
