import socket

# Client configuration
SERVER_HOST = '192.168.1.100'  # Server IP address
SERVER_PORT = 12345  # Server port

def send_script_status():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        # Send a message indicating the script is running
        client_socket.send("Script is running".encode())
    except ConnectionRefusedError:
        print("Connection to the server refused. Make sure the server is running.")
    finally:
        # Close the connection
        client_socket.close()

# Send the script status to the server
send_script_status()
