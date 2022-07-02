import socket
import sys

# create tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_host = "localhost"
server_port = 10000
server_address = (server_host, server_port)
print(f"starting up on {server_host} port {server_port}", file=sys.stderr)
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
    print("waiting for a connection", file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print(f"connection from {client_address}", file=sys.stderr)

        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(f"received {data}", file=sys.stderr)

            if data:
                print(f"sending data back to the client", file=sys.stderr)
                connection.sendall(data)

            else:
                print(f"no more data from {client_address}")
                break
    finally:
        # clean up the connection
        connection.close()
