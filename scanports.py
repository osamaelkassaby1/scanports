user1 = ["osama"]
userinput="hello"
user=input("what's your name : ")
print(userinput,user)

import os
os.system ('clear')
import socket
import sys
from time import *
from datetime import datetime
#############################
print('\033[0;31mwelcome to tool scanning ports  for osamaelkassaby')
print('\033[0;31mmy namber for whatsapp is +201555570509\033[0;31m')
print('web site is osamaelkassaby.ml')
print(userinput,user)
print("\033[0;36mThank you ",user,"for using this tool  ")
print("                                        _        ")
print("                                       | |       ")
print("   ___  ___ __ _ _ __  _ __   ___  _ __| |_ ___  ")
print("  / __|/ __/ _` | '_ \| '_ \ / _ \| '__| __/ __| ")
print("  \__ \ (_| (_| | | | | |_) | (_) | |  | |_\__ \ ")
print("  |___/\___\__,_|_| |_| .__/ \___/|_|   \__|___/ ")
print("                      | |                        ")
print("                      |_|                        ")

##############################
ip=input ("plesse..enter ip to scan ports>.. : ")
t1=datetime.now()
print ("scaning start ..%s plesse wait " %ip)
sleep(1)
############################
try:
    for port in range(1,6553):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(s.connect_ex((ip,port)) ==0):
         try:
            serv=socket.getservbyport(port)
         except socket.error:
               serv="Unknown service"

         print("port %s Open Service:%s"%(port,serv))
         t2=datetime.now()
         t3=t2-t1
         print("scanning completed On %s"%t3 )

except KeyboardInterrupt:
 print ("see you soon",user)
