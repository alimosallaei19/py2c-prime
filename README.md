# Py2c Prime

I2c interface in Python that is served over TCP that can connect to a multitude of different services. Primarily used for development in F'.

## Connecting

Py2c opens up a TCP server on port **7860** (customizable). This is not a RESTful API, rather communication of bytestreams. 

Here's an example of how you could connect to a TCP server using Python:

```py
import socket
​
#Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 7860))

while True:
​
    # Send data to server
    msg = "Message to server"
    sock.send(msg.encode('utf-8'))
​
    # Receive data from server
    data = sock.recv(1024).decode('utf-8')
    print(f"Received data: {data}")
​
    sock.close()
```
## Utilization

While not a RESTful API, data is obtained through a hierarchical system that is defined within the string sent to the server. It comes in the form of:

```txt
[endpoint]/[data to return]
```

All data is returned as a string, but then must be converted to the proper type on the client side. Information about the proper types is in the following sections.

## Endpoints

### "test" - Ping Server

Usage:      `test`
Response:   `"Hello from server.py!"`
Resp. Type: `String`

### "bme680" - All-in-One Ambience Sensor

--- get temperature ---

Usage:      `bme680/temp` 
Response:   `ex. 25.84`
Resp. Type: `Float, degC`

--- get pressure ---

Usage:      `bme680/pressure`
Response:   `ex. 500`
Resp. Type: `Float, hPa`

--- get humidity ---

Usage:      `bme680/humidity`
Response:   `ex. 40`
Resp. Type: `Int, %`

--- get all ---

Usage:      `bme680/all`
Response:   `[temp],[pressure],[humidity]`
Resp. Type: See above.

## "rm3100" - Magnetometer

--- get X measurement ---

Usage:      `rm3100/x`
Response:   `ex. ###`
Resp. Type: `Float`

--- get Y measurement ---

Usage:      `rm3100/y`
Response:   `ex. ###`
Resp. Type: `Float`

--- get Z measurement ---

Usage:      `rm3100/z`
Response:   `ex. ###`
Resp. Type: `Float`

--- get all ---

Usage:      `rm3100/all`
Response:   `[x],[y],[z]`
Resp. Type: See above.
