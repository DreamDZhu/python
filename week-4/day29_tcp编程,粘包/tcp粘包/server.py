from socket import *

sk = socket(family=AF_INET, type=SOCK_STREAM)
sk.bind(('127.0.0.1', 8000))
sk.listen()



while True:
    conn,addr = sk.accept()
    conn.send(b'alex')
    conn.send(b'hello')
    conn.send(b'111111')
    conn.close()

sk.close()























