from socket import *

# TCP 协议
#sk_tcp = socket(family=AF_INET,type=SOCK_STREAM)

# UDP协议
sk = socket(family=AF_INET, type=SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

# UDP 协议不用listen ，简单粗暴直接接收 ，使用udp协议，不能先发送信息

# UDP 协议所谓的退出，都是客户端单方面的退出
while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    print(addr)
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'), addr)

sk.close()









