import socket
import time

class Receive():
    def __init__(self, host = "", port = None, file = ""):
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server: {host}:{port}")
        
        # Open the file in binary mode for writing
        with open(file, "wb") as file:
            # Initialize variables for tracking speed
            start_time = time.time()
            print("start time" + str(start_time))
            total_bytes = 0

            # Receive and write the file data in chunks
            while True:
                chunk = client_socket.recv(1024)
                if not chunk:
                    # End of file
                    break
                # Write the chunk to the file
                file.write(chunk)

                # Update the total bytes and calculate elapsed time
                total_bytes += len(chunk)
                elapsed_time = time.time() - start_time
                print("elapsed time" + str(elapsed_time))
                
                # Calculate and display the transfer speed
                transfer_speed = total_bytes / elapsed_time
                print(f"Transfer speed: {transfer_speed:.2f} bytes/s")
        
        # Close the connection
        client_socket.close()
        print("File received successfully")

if __name__ == '__main__':
    rec = Receive("192.168.1.2", 12345, "win11.iso")