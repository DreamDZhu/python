from socket import *
import time
import struct

sk = socket(family=AF_INET, type=SOCK_STREAM)
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8000))
sk.listen()

def send_message(conn):

    msg = input('>>>')
    msg = msg.encode('utf-8')
    length = struct.pack('i', len(msg))

    print(f'msg:{msg},length:{length}')

    conn.send(length)
    conn.send(msg)
    conn.close()


while True:
    conn, addr = sk.accept()
    send_message(conn)
    # send_message(conn)
    # msg1 = input('>>>')
    # msg2 = input('>>>')
    # num = str(len(msg1))
    # num2 = str(len(msg2))
    # ret = num.zfill(4)
    # ret2 = num2.zfill(4)
    # conn.send(ret.encode('utf-8'))  # 00XX
    # conn.send(msg1.encode('utf-8')) # input info
    #
    # conn.send(ret2.encode('utf-8'))  # 00XX
    # conn.send(msg2.encode('utf-8')) # input info
    # conn.close()

sk.close()























