import socket

#Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 7860))
sock.listen(1)

print("[I2c] Py2c server started on port 7860.")

while True:

    # Accept a client connection
    client_socket, client_address = sock.accept()
    
    print(f"Client connected: {client_address}")

    # Receive data from client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    # Send data to client
    msg = "Got: " + data
    client_socket.send(msg.encode('utf-8'))

    client_socket.close()