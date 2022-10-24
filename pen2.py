import socket
import threading

host = "0.0.0.0"
port = 33333

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind((host, port))
soc.listen(5)
print(f"listening on ip:{host} and port:{port}")


def handle(client):
    request = client.recv(1024)
    print(f"recieved {request}")
    request = str(request)
    client.send(bytes(request, "utf-8"))
    client.close()


while True:
    client, addr = soc.accept()
    print(f"accepted connection from {addr[0]} {addr[1]}")
    client_handler = threading.Thread(target=handle, args=(client,))
    client_handler.start()
