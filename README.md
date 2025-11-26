# 🌐 File Transfer Application using TCP Protocol

## 🎯 Project Description
A reliable and efficient **Client–Server File Transfer System** built using **Python TCP Sockets + Flask Web Interface**.  
This project demonstrates core **Computer Networks (CN)** concepts such as TCP communication, reliability, flow control, and client–server architecture.

---

## ⭐ Features
- ✔️ Reliable TCP-based file transfer  
- ✔️ Upload only one file at a time  
- ✔️ Shows file name, file size (KB/MB), and transfer time (seconds)  
- ✔️ View & download previously received files  
- ✔️ Server terminal displays received file names  
- ✔️ Clean & attractive web interface  
- ✔️ Fully structured project for CN subject  
- ✔️ Perfect for project exhibition (30 marks)  

---

## 📂 Project Folder Structure
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
    ├── to_send/           # Uploaded files from client
    └── received/          # Files received by TCP server


---

## 🧰 Technologies Used
| Layer | Tools/Tech |
|------|-------------|
| 🎨 Frontend | HTML, CSS, JavaScript, Flask Templates |
| ⚙️ Backend | Python Flask |
| 🌐 Networking | TCP Socket Programming (socket module) |
| 💻 OS | Windows / Linux |

---

## 🛠️ How to Run the Project
🛠️ How to Run the Project
1 Start the TCP Server (Terminal 1)
python server.py


You will see:

Server running...
Waiting for incoming files...

2  Start the Web Client (Terminal 2)
python app.py


Open in browser:
👉 http://127.0.0.1:5000

3  Upload a File

Select any file

Click Upload

The file is sent to the server using TCP protocol

UI displays:

📄 File Name

📏 File Size (KB/MB)

⏱ Transfer Time (seconds)

5️⃣ View Received Files

Open:
👉 http://127.0.0.1:5000/received

All received files appear as blue clickable download links.

🧠 Why TCP? (CN Viva Answer)

TCP is used because it provides:

✔ Reliable Delivery
✔ Ordered Transmission
✔ No Data Loss
✔ Error-Free Communication
✔ Flow & Congestion Control

🔴 UDP cannot guarantee reliability, so it is not suitable for file transfer.

🔍 How the System Works
🟦 Client Side (Flask UI)

User selects a file

File is sent using a TCP socket

UI shows file name, size, and transfer time

🟥 Server Side (server.py)

Listens for incoming connections

Receives the file fully

Saves it inside files/received/

Prints file name in terminal

This clearly demonstrates a Client–Server Architecture.

👍 Advantages

✅ Reliable file transfer

✅ Simple & clear CN concept demonstration

✅ Attractive web UI

✅ Works on any OS

✅ Ideal for viva / exhibition

⚠️ Limitations

❌ Only one file at a time

❌ No authentication

❌ Not suitable for large-scale use

🚀 Future Enhancements

✨ Multi-user support
✨ Multiple file upload
✨ File encryption
✨ Live progress bar
✨ Cloud integration

📘 Conclusion

The File Transfer Application using TCP Protocol demonstrates:

✔ Reliable TCP communication
✔ Practical Client–Server networking
✔ Real file transfer mechanism
✔ Flask + Python sockets integration
✔ File size & transfer time measurement

👤 Author

✨ Geethanjali M
🎓 B.E Student — MIT Mysore
💻 Passionate about Networking & Python Development

