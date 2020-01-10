import socket
import struct

sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8000))

username = input('请输入用户名: ')
password = input('请输入密码:')

def send_msg(message):
    message = message.encode('utf-8')
    length = struct.pack('i',len(message))
    # print(length)
    # print(message)
    sk.send(length)
    sk.send(message)


send_msg(username)
send_msg(password)

length = struct.unpack('i', sk.recv(4))[0]
msg = sk.recv(length)
msg = msg.decode('utf-8')

if msg == "登录成功! 允许进行新的操作:":
    send_msg("ls")

print(msg)
