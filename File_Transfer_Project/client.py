import socket
import os
import time

HOST = '127.0.0.1'
PORT = 5002

file_path = 'files/to_send/sample.txt'
filename = os.path.basename(file_path)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(filename.encode())

    start = time.time()
    with open(file_path, 'rb') as f:
        data = f.read(1024)
        while data:
            s.send(data)
            data = f.read(1024)
    end = time.time()

print(f"[CLIENT] Sent '{filename}' successfully in {round(end - start, 2)} seconds")
