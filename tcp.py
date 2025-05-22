import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
print(f"Starting server on {server_address[0]}:{server_address[1]}")
server_socket.bind(server_address)

# Listen for incoming connections (max 5 clients in the waiting queue)
server_socket.listen(5)

while True:
    print("Waiting for a connection...")
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

        # Send a response back to the client
        response = "Hello from the server!"
        client_socket.sendall(response.encode())

    finally:
        # Close the connection
        client_socket.close()
        print(f"Connection with {client_address} closed")