```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ███████╗ █████╗  ██████╗███████╗                               ║
║   ██╔════╝██╔══██╗██╔════╝██╔════╝                               ║
║   █████╗  ███████║██║     █████╗                                 ║
║   ██╔══╝  ██╔══██║██║     ██╔══╝                                 ║
║   ██║     ██║  ██║╚██████╗███████╗                               ║
║   ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝                               ║
║                                                                  ║
║   █████╗ ████████╗████████╗███████╗███╗  ██╗██████╗              ║
║  ██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗ ██║██╔══██╗             ║
║  ███████║   ██║      ██║   █████╗  ██╔██╗██║██║  ██║             ║
║  ██╔══██║   ██║      ██║   ██╔══╝  ██║╚████║██║  ██║             ║
║  ██║  ██║   ██║      ██║   ███████╗██║ ╚███║██████╔╝             ║
║  ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝              ║
║                                                                  ║
║     📸  Your face is your ID. Walk in. You're marked.  ✅       ║
╚══════════════════════════════════════════════════════════════════╝
```
 

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Face Recognition](https://img.shields.io/badge/face__recognition-AI%20Powered-FF6B6B?style=for-the-badge)
![CSV](https://img.shields.io/badge/Database-CSV%20Reports-4ECDC4?style=for-the-badge)
![Voice](https://img.shields.io/badge/pyttsx3-Voice%20Output-FFE66D?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-C3B1E1?style=for-the-badge)

**[⭐ Star this repo](https://github.com/laraib776/Attendence-System-using-Facial-Recognition)** · **[🐛 Report a Bug](https://github.com/laraib776/Attendence-System-using-Facial-Recognition/issues)** · **[🤝 Contribute](#-contributions)**

</div>

---

## 😏 Still Taking Attendance by Hand?

> **No clipboards. No roll calls. No "here sir" chaos.**
> FaceAttend sees your students the moment they walk in — and marks them present before they even find a seat.
>
> ### 👉 **Because in 2025, your face IS the attendance sheet.** 👈
>
> *Fast. Silent. Accurate. The future of university attendance is already here.*

> [!NOTE]
> **FaceAttend** works right from your webcam — no fancy hardware needed. Just a camera, Python, and a dataset of student faces. That's it.

---

## ✦ About FaceAttend

> **FaceAttend** is a cutting-edge attendance system built for universities that replaces manual roll calls with real-time facial recognition. The moment a student is recognized by the camera, their attendance is logged automatically — no action needed from the student or the instructor.
>
> Department-wise tracking. Voice feedback. CSV reports. All out of the box.

---

##  ✨ Key Features

| 🌟 Feature | Details |
|---|---|
| 📸 **Facial Recognition** | Identifies students in real-time using the `face_recognition` library |
| ⚡ **Real-Time Attendance** | Marks attendance the instant a face is detected — zero manual effort |
| 📊 **Auto CSV Reports** | Generates downloadable attendance reports per session |
| 🏛️ **Department-Wise Tracking** | Separate attendance logs for each department |
| 🔊 **Voice Feedback** | Speaks the student's name aloud when attendance is marked |
| 🎥 **Live Camera Feed** | Displays recognized faces with name labels on screen |

---

## 🛠️ Technology Stack

```
  ╭─────────────────┬────────────────────────────────────────────╮
  │  Layer          │  Technology                                │
  ├─────────────────┼────────────────────────────────────────────┤
  │  🐍  Language   │  Python 3.x                               │
  │  👁️  Vision     │  OpenCV  (opencv-python)                  │
  │  🤖  AI / ML    │  face_recognition                         │
  │  🔊  Audio      │  pyttsx3  (text-to-speech)                │
  │  💾  Database   │  CSV files  (auto-generated reports)      │
  ╰─────────────────┴────────────────────────────────────────────╯
```

---

## 🚀 Installation & Setup

### Step 1 — Install Dependencies

```bash
pip install face_recognition opencv-python pyttsx3
```

### Step 2 — Clone the Repository

```bash
git clone https://github.com/laraib776/Attendence-System-using-Facial-Recognition.git
```

### Step 3 — Navigate into the Project

```bash
mkdir FaceAttend && cd FaceAttend
```

### Step 4 — Run the System

```bash
python main.py
```

> 💡 Make sure your webcam is connected and a student image dataset is ready before running!

---

##  🎮 Usage Guide

Once the system is running:

```
  📷  Camera starts automatically and scans for faces

  ✅  Recognized face  →  Attendance marked  +  Name displayed on screen
                       →  Voice announces the student's name

  ⌨️   Press  [ S ]    →  Mark attendance for all students at once
  ⌨️   Press  [ L ]    →  Exit the system
```

---

## 📁 Project Structure

```
📦 FaceAttend/
 │
 ├── 📄 main.py                  ← Entry point — runs the full system
 ├── 📄 README.md                ← You are here 👋
 │
 ├── 📂 dataset/                 ← Student face images (add yours here)
 │    └── 🖼️  [student_name].jpg
 │
 ├── 📂 reports/                 ← Auto-generated CSV attendance logs
 │    └── 📊 attendance_YYYY-MM-DD.csv
 │
 └── 📂 departments/             ← Department-wise attendance files
```

---

##  ⚠️ Important Notes

> [!IMPORTANT]
> **A student image dataset is required** for the facial recognition to work.
> Each student should have at least one clear, well-lit photo stored in the `dataset/` folder, named after the student.

> [!TIP]
> The system is designed for a **university setting** but can be adapted for offices, schools, or any environment with minimal changes to the configuration.

---

## 🤝 Contributions

Contributions are always welcome and appreciated! 💖

```
  1. 🍴  Fork the repository
  2. 🌿  Create your feature branch
  3. 💾  Commit your changes
  4. 📬  Open a Pull Request
```

Whether it's improving accuracy, adding a new report format, or building a web dashboard on top — all ideas are welcome!

---

##  📜 License

This project is open source under the **MIT License** — free to use, modify, and share.

---

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     No clipboards.  No shouting names.  No drama.        ║
║                                                          ║
║      Just walk in.  Your face does the rest.  📸 ✅     ║
║                                                          ║
║            Made with ❤️  by  Laraib Khalid              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

*⭐ Drop a star if FaceAttend saved your attendance sheet!*

</div>
