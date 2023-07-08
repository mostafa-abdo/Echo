import socket
import time
import os

class Send():
    def __init__(self, host = "", port = None, file_path = ""):

        sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.bind((host, port))
        sock.listen(1)

        print(f"Server listening on {host}:{port}")

        client_sock, addr = sock.accept()

        print(f"Connected to client: {addr}")

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
                client_sock.send(chunk)

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
        client_sock.close()
        sock.close()
        print("File sent successfully")

if __name__ == '__main__':
    send = Send("0.0.0.0", 12345, "win11.iso")