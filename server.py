import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",12343)) # use socket.gethostname() to use in local network
s.listen(5)

while True:
    
    clientsocket,address = s.accept()
    print(f'Connection from {address}')
    clientsocket.send(bytes("Server is connected","utf-8"))
    
    while True:
        inp = input("Command: ")
        clientsocket.send(bytes(inp,"utf-8"))
        mes = clientsocket.recv(1024).decode("utf-8")
        print(mes)
