import socket
import os
import time

HOST = '127.0.0.1'
PORT = 5002  # instead of 5001


os.makedirs('files/received', exist_ok=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"[SERVER] Listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"[CONNECTED] {addr}")
    filename = conn.recv(1024).decode()
    file_path = os.path.join('files/received', filename)
    
    start_time = time.time()
    with open(file_path, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    
    end_time = time.time()
    print(f"[SUCCESS] Received '{filename}' in {round(end_time - start_time, 2)}s")
    conn.close()
