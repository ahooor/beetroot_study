import socket

def caesar_cipher(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + key - shift) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text


def main():
    server_address = ('127.0.0.1', 12345)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print("Connected to", client_address)

    data = client_socket.recv(1024).decode()
    while data:
        key = int(client_socket.recv(1024).decode())

        encrypted_data = caesar_cipher(data, key)
        client_socket.send(encrypted_data.encode())

        data = client_socket.recv(1024).decode()

    client_socket.close()
    server_socket.close()

