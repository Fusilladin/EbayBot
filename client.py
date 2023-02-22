import socket 

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("0.tcp.sa.ngrok.io",13481))

print(client.recv(1024).decode())
client.send("Hey Server".encode())


