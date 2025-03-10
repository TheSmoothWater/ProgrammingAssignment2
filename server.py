import socket
import os
import sys

IP = '127.0.0.1'  # default IP address of the server
PORT = 12000  # change to a desired port number
BUFFER_SIZE = 1024  # change to a desired buffer size

#Doesn't work as expected
def get_file_info(data: str) -> (str, int):
    seperator = data.find(",")
    print(f"Data: {data}")
    file_size = bytes.fromhex(data[2:seperator - 1].replace("\\x", ""))
    file_size = int.from_bytes(file_size, byteorder="big")
    print(f"Method File Size: {file_size}")

    file_name = data[seperator + 1:]
    print(f"File name: {file_name}")

    return file_name, file_size


def upload_file(conn_socket: socket, file_name: str, file_size: int):
    # create a new file to store the received data
    file_name += '.temp'
    # please do not change the above line!
    with open(file_name, 'wb') as file:
        retrieved_size = 0
        print(f"File Size: {file_size}")
        try:
            while retrieved_size < file_size:
                # TODO: section 1 step 6a
                data = conn_socket.recv(BUFFER_SIZE)
                # TODO: section 1 stop 6b
                retrieved_size += len(data)
                # TODO: section 1 stop 6c
                file.write(data)
                # print(f"Retrieved Size: {retrieved_size}")

        except OSError as oe:
            print(oe)
            os.remove(file_name)

def start_server(ip, port):
    # create a TCP socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print(f'Server ready and listening on {ip}:{port}')

    try:
        while True:
            conn_socket, addr = server_socket.accept()
            # TODO: section 1 step 2
            # expecting an 8-byte byte string for file size followed by file name
            recvBytes, address = conn_socket.recvfrom(BUFFER_SIZE)
            print("We received File Name")
            # TODO: section 1 step 3

            file_info = recvBytes.decode()

            file_name, file_size = get_file_info(file_info)

            print(f'Received: {file_name} with size = {file_size}')
            # TODO: section 1 step 4
            conn_socket.sendto(b'go ahead', addr)
            upload_file(conn_socket, file_name, file_size)
            conn_socket.close()
    except KeyboardInterrupt as ki:
        pass
    finally:
        server_socket.close()


if __name__ == '__main__':
    # get IP address from cmd line if provided
    if len(sys.argv) == 2:
        IP = sys.argv[1]  # IP from cmdline argument

    try:
        # get port number from cmd line if provided
        if len(sys.argv) == 3:
            PORT = int(sys.argv[2])  # IP from cmdline argument
    except ValueError as ve:
        print(ve)
    start_server(IP, PORT)