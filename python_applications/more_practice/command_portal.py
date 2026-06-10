import socket, sys


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8500))
server_socket.listen(1)

mock_inventory = {"101": "Introduction to Python", "102": "Systems Architecture"}
client_socket, client_address = server_socket.accept()
while True:

    incoming_message = client_socket.recv(1024)
    decoded_message = incoming_message.decode()
    if decoded_message in mock_inventory:
        client_socket.sendall(mock_inventory[decoded_message])
    else:
        pass

client_socket.close()
server_socket.close()