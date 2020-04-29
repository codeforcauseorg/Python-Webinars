import socket
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket object
CHUNK = 65535
# instead of explicitly binding the socket, i will let OS do it.
# ephemaral ports
# OS will bind this for us
hostname = '127.0.0.1'
while True:
    s.connect((hostname, port))
    message = input("Type message: ")
    data = message.encode("ascii")
    s.send(data)
    # data received:
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f'Kunal: {text}')
