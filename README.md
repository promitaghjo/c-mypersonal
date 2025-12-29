# 🎓 Smart Exam Cheating Detection System

**AI-Based Online Proctoring using Computer Vision & Deep Learning**

---

## 📌 Overview

The **Smart Exam Cheating Detection System** is an AI-powered proctoring solution designed to monitor online examinations in real time.
It uses **computer vision and deep learning** to detect suspicious behaviors such as:

* Absence of student
* Presence of multiple people
* Mobile phone usage during exams

The system automatically **logs cheating events** and **captures visual evidence** with timestamps for audit and review.

---

## 🚀 Features

* 🎥 **Real-time webcam monitoring**
* 🙂 **Face detection** using Haar Cascades
* 📱 **Mobile phone detection** using YOLOv8
* 📊 **Cheating confidence score (0–100%)**
* 📸 **Automatic screenshot capture** for evidence
* 📝 **CSV-based event logging**
* ⏱️ **Cooldown mechanism** to prevent duplicate evidence
* 💻 **Lightweight & runs locally**

---

## 🧠 Technologies Used

| Category             | Tools                   |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Computer Vision      | OpenCV                  |
| Deep Learning        | YOLOv8 (Ultralytics)    |
| Face Detection       | Haar Cascade Classifier |
| Logging              | CSV                     |
| Environment          | VS Code, Windows        |
| Hardware             | Webcam                  |

---

## 📂 Project Structure

```
c-mypersonal/
│
├── face_detection.py        # Main detection system
├── app.py                   # (Optional) Web dashboard
│
├── logs/
│   └── cheating_log.csv     # Cheating event logs
│
├── evidence/
│   └── *.jpg                # Screenshot evidence
│
├── yolo/
│   └── yolov8n.pt           # YOLO model
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/c-mypersonal.git
cd c-mypersonal
```

### 2️⃣ Install dependencies

```bash
pip install opencv-python ultralytics
```

### 3️⃣ Download YOLOv8 model

Place `yolov8n.pt` inside the project folder.

---

## ▶️ How to Run

```bash
python face_detection.py
```

* Webcam opens automatically
* Press **`Q`** to exit
* Screenshots saved in `evidence/`
* Logs saved in `logs/cheating_log.csv`

---

## 📊 Cheating Detection Logic

| Condition        | Score   |
| ---------------- | ------- |
| No face detected | +40     |
| Multiple faces   | +50     |
| Phone detected   | +60     |
| **Max Score**    | **100** |

If **cheating score ≥ 60%**:

* Screenshot is captured
* Event is logged with timestamp

---

## 📸 Sample Log Entry

```
2025-12-29 11:01:43,PHONE_DETECTED,100,evidence/20251229_110425_PHONE_DETECTED.jpg
```

---

## 🎯 Use Cases

* Online exams & assessments
* Remote interviews
* Proctored certification tests
* Academic integrity monitoring

---

## 🔮 Future Enhancements

* Head movement & gaze tracking
* Audio-based cheating detection
* Live web dashboard (Flask)
* Cloud storage for evidence
* Multi-student classroom mode

---

## 🎓 Academic Value

This project demonstrates:

* Practical AI & ML application
* Real-time system design
* Ethical AI monitoring
* Industry-grade logging & evidence handling

---

## 🧑‍💻 Author

**Promita Ghosh**
2nd Year CSE Student
📌 Aspiring Software Engineer & AI Developer

---

## ⭐ Acknowledgements

* OpenCV Community
* Ultralytics YOLO
* Python Software Foundation

---

## 📜 License

This project is for **educational purposes**.

---


