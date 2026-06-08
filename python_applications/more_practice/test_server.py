import socket, sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 7777))

server_socket.listen(1)

print("[Server] Waiting for an external connection on Port 7777...")


client_connection, client_address = server_socket.accept()
print(f"[Server] Connected to a client at: {client_address}")


incoming_data = client_connection.recv(1024)
decoded_text = incoming_data.decode().strip()


print(f"[Server] Received Message: '{decoded_text}'")

client_connection.close()
server_socket.close()