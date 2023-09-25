import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        print("Received data from {}: {}".format(client_socket.getpeername(), data.decode()))

        client_socket.send(data)

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

print("UDP server is at {}:{}".format(*server_address))

while True:
    data, client_address = server_socket.recvfrom(1024)
    print("Accepted connection from {}: {}".format(client_address, data.decode()))

    client_thread = threading.Thread(target=handle_client, args=(server_socket,))
    client_thread.start()
