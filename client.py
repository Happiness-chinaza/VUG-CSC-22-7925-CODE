import socket

def start_client():
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # localhost
    port = 12345
    
    # Connect to server
    client_socket.connect((host, port))
    print("Connected to server")
    
    while True:
        # Send message to server
        message = input("Client message: ")
        client_socket.send(message.encode())
        
        # Check for stop command
        if message.lower() == "stop":
            print("Stopping client...")
            break
            
        # Receive reply from server
        reply = client_socket.recv(1024).decode()
        print(f"Server: {reply}")
        
        # Check if server sent stop
        if reply.lower() == "stop":
            print("Server requested stop. Closing client...")
            break
    
    # Clean up
    client_socket.close()

if __name__ == "__main__":
    start_client()
