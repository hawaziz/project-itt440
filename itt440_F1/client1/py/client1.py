import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 8080))

message = "Hello Server!"
clientSocket.send(message.encode())

response = clientSocket.recv(1024)
print("Server response:", response.decode())

clientSocket.close()
