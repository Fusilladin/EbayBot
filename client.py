import socket 

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("0.tcp.sa.ngrok.io",11111))

print(client.recv(1000).decode())
client.send("Hey Server".encode())


