import time
import socket

#Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 7860))

while True:
    # Send data to server
    msg = "bme680/all"
    sock.send(msg.encode('utf-8'))

    # Receive data from server
    data = sock.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    time.sleep(1)
