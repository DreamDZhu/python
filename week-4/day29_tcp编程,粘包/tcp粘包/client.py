import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8000))

length = sk.recv(4)
length = struct.unpack('i', length)[0]

msg = sk.recv(length) # 999999999

msg = msg.decode('utf-8')


print(f'msg:{msg} length:{length}')


# 10mb
# 先获取文件大小
# 读取一个数据