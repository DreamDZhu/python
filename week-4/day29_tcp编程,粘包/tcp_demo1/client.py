import socket
from conf import settings as SETTINGS

sk = socket.socket()
sk.connect(SETTINGS.CONNECT)

while True:
    # 接收信息
    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':
        break
    print(msg)

    # 发送信息
    send_msg = input('>>>').encode('utf-8')
    sk.send(send_msg)
    if send_msg.upper() == 'Q':
        break

sk.close()


















