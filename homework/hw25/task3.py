import socket
import multiprocessing

def handle_client(data, client_address):
    print("Received data from {}: {}".format(client_address, data.decode()))

    response = "Hello, client!"
    server_socket.sendto(response.encode(), client_address)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

print("UDP server is at {}:{}".format(*server_address))

while True:
    data, client_address = server_socket.recvfrom(1024)
    print("Accepted connection from {}:{}".format(*client_address))

    client_process = multiprocessing.Process(target=handle_client, args=(data, client_address))
    client_process.start()
