import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)

while True:
    message = input("Enter a message to send to the server (or 'exit' to quit): ")
    if message == 'exit':
        break

    client_socket.sendto(message.encode(), server_address)

    response, server = client_socket.recvfrom(1024)
    print("Received response from {}: {}".format(server, response.decode()))

client_socket.close()
