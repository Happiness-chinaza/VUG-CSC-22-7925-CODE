import socket

def start_server():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # localhost
    port = 12345

    # Bind and listen
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept client connection
    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")

    while True:
        # Receive message from client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        # Check for stop command
        if data.lower() == "stop":
            print("Stopping server...")
            break

        # Send reply to client
        reply = input("Server reply: ")
        conn.send(reply.encode())

        # Check if server wants to stop
        if reply.lower() == "stop":
            print("Stopping server...")
            break

    # Clean up
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
