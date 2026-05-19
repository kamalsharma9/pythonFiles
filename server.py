import socket

# Define server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (use > 1023)

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind the socket to the host and port
    s.listen()             # Start listening for incoming connections
    print(f"Server is listening on {HOST}:{PORT}...")
    
    conn, addr = s.accept()  # Block and wait for a connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  # Receive data (up to 1024 bytes)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(data)      # Echo the data back to the client

