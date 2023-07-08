import socket
import uuid
import pickle

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_device_info():
    # Get the device name
    device_name = socket.gethostname()

    # Get the MAC address
    mac_address = ':'.join(format(c, '02x') for c in uuid.getnode().to_bytes(6, 'big'))

    return {"device_name": device_name, "mac_address": mac_address}


def start_server(HOST, PORT):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server is listening on {HOST}:{PORT}")
    
    while True:
        try:
            # Accept a new connection
            client_socket, addr = server_socket.accept()
            print(f"New connection from {addr[0]}:{addr[1]}")
            device_info = get_device_info()
            client_socket.sendall(pickle.dumps(device_info))
        except:
            print('There is an error.')
        finally:
            # Close the connection
            client_socket.close()



if __name__ == '__main__':
    # Server configuration
    HOST = get_ip_address()  # Server IP address
    PORT = 12345  # Server port


    # Start the server
    start_server(HOST, PORT)
