import socket
from sensors.bme680_sensor import BME680
from sensors.rm3100_sensor import RM3100

#Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 7860))
sock.listen(1)

print("[I2c] Py2c server started on port 7860.")

# initialize custom sensor classes
bme680 = BME680()
rm3100 = RM3100()

def test():
    return "Hello from server.py!"

while True:
    # Accept a client connection
    client_socket, client_address = sock.accept()
    
    print(f"Client connected: {client_address}")

    # Receive data from client
    data = client_socket.recv(1024).decode('utf-8')
    data = data.split("/")
    response = ""

    # first element of data should be the "endpoint"
    if data[0] == "test":
        response = test()
    elif data[0] == "bme680":
        if data[1] == "temp":
            response = str(bme680.get_temp())
        elif data[1] == "pressure":
            response = str(bme680.get_pressure())
        elif data[1] == "humidity":
            response = str(bme680.get_humidity())
        elif data[1] == "all":
            response = str(bme680.get_temp()) + "," + str(bme680.get_pressure()) + "," + str(bme680.get_humidity())
    elif data[0] == "rm3100":
        if data[1] == "x":
            response = str(rm3100.get_x())
        elif data[1] == "y":
            response = str(rm3100.get_y())
        elif data[1] == "z":
            response = str(rm3100.get_z())
        elif data[1] == "all":
            response = str(rm3100.get_x()) + "," + str(rm3100.get_y()) + "," + str(rm3100.get_z())

    client_socket.send(response.encode('utf-8'))

    #client_socket.close()