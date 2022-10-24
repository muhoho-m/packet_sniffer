#!/usr/bin/env python

import sys
import socket
import threading


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except:
        print(f"[!!] Failed to listen on {local_host} and {local_port}")
        print(f"check for listening sockets or correct permissions")
        sys.exit()
    print(f"[*] listening on {local_host} {local_port}")
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        # print out the local connection info
        print(f"[==>] receiving connection from {addr[0]}:{addr[1]}")
        # start thread to talk to the remote host
        proxy_thread = threading.Thread(target=proxy_handler, agrs=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()


def main():

