# socket-client-test.py

import socket
import time

HOST = "server"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

print(f"Attempting to connect to {HOST} on port {PORT}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    time.sleep(2) # this was only added in case it was connecting too fast for the server to set up first
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
