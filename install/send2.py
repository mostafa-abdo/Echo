import socket
import time
import os
from install.test4 import SendReg

class Send():
    def __init__(self, host = "", port = None, file_path = ""):

        sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.connect((host, port))

        print(f"connected to {host}:{port}")

        file_name = os.path.basename(file_path)
        file_name = file_name
        print("filename: " + file_name)

        sock.send(file_name.encode(errors='ignore'))

        with open(file_path, "rb") as file:
            # Initialize variables for tracking speed
            start_time = time.time()
            print("start time: " + str(start_time))

            total_bytes = 0

            # Read and send the file data in chunks
            while True:
                chunk = file.read(8129*7000)
                if not chunk:
                    # End of file
                    break
                # Send the chunk to the client
                sock.send(chunk)

                # Update the total bytes and calculate elapsed time
                total_bytes += len(chunk)
                elapsed_time = time.time() - start_time
                print("elapsed time: " + str(elapsed_time))

                if elapsed_time == 0:
                    print("Zerooooo")
                    continue
                file_size = os.path.getsize(file_path)
                print("file size: "+str(file_size))
                # Calculate and display the transfer speed
                transfer_speed = total_bytes / (elapsed_time * 1024 * 1024)
                remaining_bytes = file_size - total_bytes
                estimated_time_left = remaining_bytes / (transfer_speed * 1024 * 1024)

                # Display transfer speed and estimated time left
                print(f"Transfer speed: {transfer_speed:.2f} MB/s")
                print(f"Estimated time left: {estimated_time_left:.2f} seconds")



    
        # Close the connection
        sock.close()
        print("File sent successfully")
        time.sleep(10.0)
        SendReg('Audacity')
        print('Registry Sent successfully.')
