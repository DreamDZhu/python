import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 8000))

#time.sleep(0.1)

msg1 =sk.recv(1024)
msg2 =sk.recv(1024)

print(msg1)
print(msg2)











