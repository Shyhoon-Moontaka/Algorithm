import socket
s = socket.socket()
s.bind(('localhost',3000))
s.listen()
client,addr=s.accept()
while True:
    info = input("From Server: ").encode()
    client.send(info)
    data = client.recv(1024).decode()
    print(data)