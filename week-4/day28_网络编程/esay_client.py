from socket import *

HOST = 'localhost'
PORT = 8080

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(b'Hello,world')

data = client.recv(1024)
print('Received', data)
