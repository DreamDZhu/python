import socket

CONNECT = ("127.0.0.1", 7000)

sk = socket.socket()
sk.connect(CONNECT)

msg = sk.recv(1024) #最多接收1024字节
print(msg)
sk.send(b'byebye')
sk.close()
















