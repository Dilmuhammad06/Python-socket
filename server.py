import socket

MY_IP = input("IP: ")
MY_PORT = input("PORT: ")

if len(str(MY_IP)) > 0 and len(str(MY_PORT)) > 0:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((MY_IP,int(MY_PORT)))
    s.listen(5)
    
    print(f"Server is on {MY_IP}:{MY_PORT}")
    
    while True:
        clientsocket,address = s.accept()
        print(f'Connection from {address}')
        clientsocket.send(bytes("Server is connected","utf-8"))
        
        while True:
            inp = input("Command: ")
            clientsocket.send(bytes(inp,"utf-8"))
            mes = clientsocket.recv(1024).decode("utf-8")
            print(f"\n\n{mes}")
else:
    print("There is a problem with IP or PORT")
