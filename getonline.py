import socket
import pickle



class GetOnline():
    def __init__(self, network, port = 12345):
        # Client configuration
        SERVER_HOST = network  # Server IP address
        SERVER_PORT = port  # Server port

        self.devices_data = []

        h = 0

        while True:

            h += 1

            if h >= 10:
                break

            host = SERVER_HOST + str(h)
            print(host)

            # Send the script status to the server
            self.send_script_status(host, SERVER_PORT)


    def send_script_status(self, SERVER_HOST, SERVER_PORT):
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(.3)
        
        try:
            # Connect to the server
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            data = client_socket.recv(1024)
            if data:
                data = pickle.loads(data)
                client_device_name = data['device_name']
                client_device_mac = data['mac_address']
                self.devices_data.append([client_device_name.upper(), client_device_mac.upper(), SERVER_HOST])
                print(client_device_name)
                print(client_device_mac)
            
        except:
            print("Connection to the server refused. Make sure the server is running.")
        finally:
            # Close the connection
            client_socket.close()
