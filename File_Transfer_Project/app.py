from flask import Flask, render_template, request, redirect, send_from_directory
import os
import socket
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'files/to_send'
RECEIVE_FOLDER = 'files/received'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RECEIVE_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    HOST, PORT = '127.0.0.1', 5002
    start_time = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(file.filename.encode())
        with open(file_path, 'rb') as f:
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)

    end_time = time.time()
    transfer_time = round(end_time - start_time, 2)
    file_size = round(os.path.getsize(file_path) / 1024, 2)  # KB

    return render_template('success.html', filename=file.filename, size=file_size, time=transfer_time)

@app.route('/received')
def received_files():
    files = os.listdir(RECEIVE_FOLDER)
    return render_template('received.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(RECEIVE_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
