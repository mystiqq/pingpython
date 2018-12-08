import socket
import sys
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = raw_input("Enter server IP : ")
rep = os.system("ping " + server_ip)
if rep == 0:
	print("Data sucessfuly sent!")
else:
	print("error")