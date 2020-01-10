import socket
import struct
import os

sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 8000))
sk.listen()

userinfo_dict = {}


def load_info():
    with open('user.txt', mode='r') as f:
        for line in f:
            if line:
                username, password = line.split(',')
                username = username.strip().strip('\n')
                password = password.strip().strip('\n')
                if username not in userinfo_dict:
                    userinfo_dict[username] = password
                else:
                    print('username repeat')


if __name__ == '__main__':
    load_info()


def send_msg(message):
    message = message.encode('utf-8')
    length = struct.pack('i', len(message))
    conn.send(length)
    conn.send(message)


def recv_msg():
    length = struct.unpack('i', conn.recv(4))[0]
    username = conn.recv(length).decode('utf-8')
    length = struct.unpack('i', conn.recv(4))[0]
    password = conn.recv(length).decode('utf-8')
    return (username, password)

def recv_one():
    length = struct.unpack('i', conn.recv(4))[0]
    msg = conn.recv(length).decode('utf-8')
    return msg

while True:
    conn, addr = sk.accept()
    info = recv_msg()

    print(info)

    if info[0] in userinfo_dict:
        if userinfo_dict[info[0]] == info[1]:
            send_msg("登录成功! 允许进行新的操作:")
            msg = recv_one()
            os.system(msg)

        else:
            send_msg("密码错误！！")
            conn.close()
    else:
        send_msg("账户不存在,连接断开")
        conn.close()


sk.close()
