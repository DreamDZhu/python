import socket

BIND = ("127.0.0.1", 7000)

sk = socket.socket()      # 实例化
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 端口释放
sk.bind(BIND)             # 绑定ip + 端口
sk.listen()               # 开启监听

# # 接收客户端连接
# # 当客户端连接后，可以获取到该连接 conn , 和对方的地址 addr
# conn, addr = sk.accept()
# print('coon: ',conn)
#
# # conn 中存储的是什么 ？
# # conn 中存储的是一个客户端和Server 的连接信息
#
# conn.send(b'hello')  # 向客户端发送信息
# msg = conn.recv(1024)     # 一次最多接收1024字节的信息
# print(msg)
# conn.close()        # 断开这次连接

# 为了和多个客户端进行握手

while True:
    conn, addr = sk.accept()

    print('--------------------')
    print("conn: ", conn)
    print('--------------------')
    # 为了跟这个客户端一直沟通
    while True:
        # 发送信息
        send_msg = input('>>>')
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':
            break

        # 接收信息
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == 'Q':
            break
        print(msg)

    conn.close()



sk.close()          # 关闭服务端 , 归还申请的操作系统资源

# conn.send 中，双方使用的编码必须一致，否则解析会出现问题
# str -encode('utf-8') -> bytes
# str -encode('gbk')   -> bytes
"""
你 字符
utf-8 b'181921'
gbk   b'17210'
"""
