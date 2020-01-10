import socket
import time

UDP_SERVER = ('127.0.0.1',8000)
name = ""

class Socker_client:

    def __init__(self):
        self.sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.name = None

    def run(self):
        while True:
            if not self.name:
                self.name = input("欢迎使用匿名聊天室，请输入想使用的姓名: ").strip()
                self.send(self.name)

            time.sleep(0.2)

            msg = self.recv()
            print(msg)


            # msg = input('>>>')
            # self.send(msg)



    def send(self,msg):
        msg = msg.encode('utf-8')
        self.sk.sendto(msg, UDP_SERVER)

    def recv(self):
        return self.sk.recv(1500).decode('utf-8')

sk = Socker_client()
sk.run()

# while True:
#     if name:
#         name = input("请输入要使用的姓名: ")
#         if name.upper() == 'Q':
#             send_msg
#
#     send_msg = input('>>>')
#     if send_msg.upper() == 'Q':
#         break
#     sk.sendto(send_msg.encode('utf-8'), SERVER)
#     msg = sk.recv(1024).decode('utf-8')
#     if msg.upper() == 'Q':
#         break
























