from socket import *
import time

SERVER = ('127.0.0.1',9000)
sk = socket(family=AF_INET, type=SOCK_DGRAM)

while True:
    send_msg = input('>>>')
    if send_msg.upper() == 'Q':
        break
    sk.sendto(send_msg.encode('utf-8'), SERVER)
    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':
        break

