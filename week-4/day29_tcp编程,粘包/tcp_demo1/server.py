import socket

BIND = ("127.0.0.1", 7000)

sk = socket.socket()      # 实例化
sk.bind(BIND)             # 绑定ip + 端口
sk.listen()               # 开启监听

# 接收客户端连接
# 当客户端连接后，可以获取到该连接 conn , 和对方的地址 addr
conn, addr = sk.accept()
print('coon: ',conn)

# conn 中存储的是什么 ？
# conn 中存储的是一个客户端和Server 的连接信息

conn.send(b'hello')  # 向客户端发送信息
msg = conn.recv(1024)     # 一次最多接收1024字节的信息
print(msg)
conn.close()        # 断开这次连接


sk.close()          # 关闭服务端 , 归还申请的操作系统资源
