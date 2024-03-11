import socket

while True:
    s = socket.socket()
    s.connect(('192.168.140.130',3000))

    info = input("Enter a message: ")
    s.send(info.encode())

    data = s.recv(1024)
    if not data:
        break
    print(data.decode())

s.close()