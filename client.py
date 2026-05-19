import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The same port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    s.sendall(b"Hello, server!")  # Send message (encoded as bytes)
    data = s.recv(1024)           # Receive response

print(f"Received from server: {data.decode()}")

