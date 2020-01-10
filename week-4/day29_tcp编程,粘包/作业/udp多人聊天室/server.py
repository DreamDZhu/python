import socket
import time

# 'address' : 'name'
addr_lst = {}

class Socker_server:

    def __init__(self, ip, host):
        self.sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sk.bind((ip, host))

    def run(self):
        while True:

            info = self.recv()
            # msg = msg.decode('utf-8')
            msg = info[0]
            addr = info[1]
            # 说明第一次连接
            if addr not in addr_lst:
                # 接收姓名
                addr_lst[addr] = msg
                self.send("==================================", addr)
                self.send(f"=========欢迎{msg}来到匿名聊天室==========", addr)
                self.send("===========可以开始畅聊=============", addr)
            else:
                # 不是第一次连接 再说
                print(f"{addr_lst[addr]} speak:{msg}")

            print(addr_lst)
            time.sleep(0.2)




    def send(self, msg, addr):
        msg = msg.encode('utf-8')
        self.sk.sendto(msg, addr)

    def recv(self):
        msg, addr = self.sk.recvfrom(1500)
        return [msg.decode('utf-8'), addr]

sk = Socker_server('127.0.0.1',8000)
sk.run()



# 多人聊天室 那服务器就是一个中转站
# while True:
#     msg, addr = sk.recvfrom(1024)
#     msg = msg.decode('utf-8')

    # 说明第一次连接
# if addr not in addr_lst:

        # print(msg.decode('utf-8'))
        # print(addr)

        # send_msg = input('>>>')
        # sk.sendto(send_msg.encode('utf-8'), addr)
