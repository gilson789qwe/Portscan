#Projeto port Scan
#Classe de comandos do projeto port

import socket, sys

ip = "192.168.43.1"
porta= 80

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res = sock.connect_ex((ip,porta))

if (res == 0):
    print("Aberta")
    sock.close()
else:
    print("Fechada")
    sock.close()