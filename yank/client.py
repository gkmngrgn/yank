import socket


def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict((getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix))


families = get_constants("AF_")
types = get_constants("SOCK_")
protocols = get_constants("IPPROTO_")

# create a tcp/ip socket
server_host = "localhost"
server_port = 10000
server_address = (server_host, server_port)
sock = socket.create_connection((server_host, server_port))

print(f"Family  : {families[sock.family]}")
print(f"Type    : {types[sock.type]}")
print(f"Protocol: {protocols[sock.proto]}")
print()

try:
    # send data
    message = b"This is the message. It will be repeated."
    sock.sendall(message)

    # look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"received {data}")

finally:
    sock.close()
