import socket


sk = socket.socket()
sk.connect(("127.0.0.1", 7000))

msg = sk.recv(1024) #最多接收1024字节
print(msg.decode('utf-8'))
sk.send("byebye".encode('utf-8'))
sk.close()
















