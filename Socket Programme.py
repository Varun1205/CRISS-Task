import socket

serverIP = '172.17.29.11'
serverPORT = 6000
serveradress = (serverIP, serverPORT)
bufferSize = 1024
   
LDPCClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

message = 'Hi my name is Varun Saboo my ID is 2022AAPS0215P'

bytestosend = str.encode(message)

LDPCClientSocket.sendto(bytestosend, serveradress)