import socket

def main():
    server_address = ('127.0.0.1', 12345)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    key = int(input("Enter the Caesar cipher key: "))
    client_socket.send(str(key).encode())

    while True:
        message = input("Enter a message to send to the server (or 'exit' to quit): ")
        if message == 'exit':
            break

        client_socket.send(message.encode())
        encrypted_response = client_socket.recv(1024).decode()
        print("Received encrypted response:", encrypted_response)

    client_socket.close()

