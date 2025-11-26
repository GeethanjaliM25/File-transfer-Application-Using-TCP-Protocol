🌐 File Transfer Application using TCP Protocol

🎯 Project Description

A reliable and efficient Client–Server File Transfer System built using Python TCP Sockets + Flask Web Interface.
This project demonstrates core Computer Networks (CN) concepts such as TCP communication, reliability, flow control, and client–server architecture.

⭐ Features

✔️ Reliable TCP-based file transfer
✔️ Upload only one file at a time
✔️ Shows file name, size (KB/MB), transfer time (seconds)
✔️ View & download previously received files
✔️ Server terminal displays received file names
✔️ Clean & attractive web interface
✔️ Fully structured project for CN subject
✔️ Perfect for project exhibition (30 marks)

📂 Project Folder Structure
File_Transfer_Project/
│
├── app.py                 # Flask Web Client (Frontend)
├── server.py              # TCP Server Backend
├── client.py              # Optional CLI Client
│
├── templates/
│   ├── index.html
│   ├── success.html
│   └── received.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── files/
    ├── to_send/           # Uploaded files
    └── received/          # Server-received files

🧰 Technologies Used
Layer	Tools/Tech
🎨 Frontend	HTML, CSS, JavaScript, Flask Templates
⚙️ Backend	Python Flask
🌐 Networking	TCP Socket Programming (socket module)

💻 OS	Windows / Linux
🛠️ How to Run the Project
1️⃣ Install Flask
pip install flask

2️⃣ Start the TCP Server (Terminal 1)
python server.py

✔ Shows:
Server running...
Waiting for incoming files...

3️⃣ Start the Web Client (Terminal 2)
python app.py

Open in browser:
👉 http://127.0.0.1:5000

4️⃣ Upload a File

Choose any file

Click Upload

TCP sends file to server

Displays:

📄 File Name

📏 File Size

⏱ Transfer Time

5️⃣ View Received Files

Open:
👉 http://127.0.0.1:5000/received

All files appear as blue clickable links.

🧠 Why TCP? (For CN Viva)

TCP is used because it provides:

✔ Reliable Delivery
✔ No data loss
✔ Ordered transmission
✔ Error-free communication
✔ Congestion & flow control

File transfer cannot tolerate missing or damaged data, hence TCP is the best choice.
UDP ❌ cannot guarantee reliability.

🔍 How the System Works
🟦 Client Side (Flask UI)

User selects file

File is sent through TCP

UI shows:

Filename

Size

Transfer Time

🟥 Server Side (server.py)

Listens for clients

Receives file completely

Saves into files/received/

Prints name in terminal

This forms a clear Client–Server Architecture.

👍 Advantages

✅ Reliable file transmission
✅ Simple & clear CN demonstration
✅ Attractive UI
✅ OS independent
✅ Perfect for viva/exhibition

⚠️ Limitations

❌ Only one file at a time
❌ No authentication
❌ Not suitable for large-scale use

🚀 Future Enhancements

✨ Multi-user system
✨ Multiple file upload
✨ File encryption
✨ Progress bar sync
✨ Cloud integration

📘 Conclusion

The File Transfer Application using TCP Protocol successfully demonstrates:

✔ Reliable TCP communication
✔ Real client–server networking
✔ Practical file transmission
✔ Flask + Python socket integration
✔ Real-time file size/time measurement

This project is ideal for Computer Networks (CN) mini-projects, exhibitions, and viva demonstrations.
It clearly shows how TCP ensures safe, accurate, and ordered file transfer.

👤 Author

✨ Geethanjali M
🎓 B.E Student — MIT MYSORE 
💻 Passionate about Networks & Python
