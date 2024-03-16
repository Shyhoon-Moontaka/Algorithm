import socket
s = socket.socket()
s.connect(('147.185.221.18',61463))
while True:
    data = s.recv(1024).decode()
    print(data)
    info = input("From Client: ").encode()
    s.send(info)