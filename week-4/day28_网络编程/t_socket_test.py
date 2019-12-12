from socket import *
import time

'''
family = AF_UNIX / AF_INET
type = SOCK_STREAM / SOCK_DGRAM
proto = 0

'''

sk = socket()
sk.bind(("127.0.0.1", 8080))  # 套接字监听
sk.listen(5)

while True:
    conn, address = sk.accept()
    time.sleep(1)
    sk.sendall(bytes("hello world", encoding="utf-8"))


# def t_sock():
#     # 创建TCP 套接字
#     tcpSock = socket(AF_INET, SOCK_STREAM)
#     # 创建UDP/IP 套接字
#     udpSock = socket(AF_INET, SOCK_DGRAM)
