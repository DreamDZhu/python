import socket

HOST = '127.0.0.1'
PORT = 8080

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind((HOST, PORT))

sock_server.listen(5)
conn, addr = sock_server.accept()

with conn:
    print('Connect by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

