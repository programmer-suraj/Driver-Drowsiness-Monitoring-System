# 🚗 Driver Drowsiness Monitoring System

A real-time AI-based system that detects driver fatigue using computer vision techniques and alerts the user to prevent accidents. The system analyzes facial landmarks to monitor eye closure and yawning patterns using lightweight and efficient models.

---

## 🔥 Features

* 👁️ Eye Aspect Ratio (EAR) based drowsiness detection
* 😮 Mouth Aspect Ratio (MAR) based yawning detection
* 🔊 Real-time audio alert system
* 🎥 Live video streaming via web interface
* 📊 Real-time metrics display (EAR & MAR)
* 📝 Event logging (CSV-based tracking)
* ⚡ Optimized performance (no dlib dependency)
* 🌐 Flask-based web dashboard

---

## 🧠 How It Works

1. Captures live video from webcam
2. Detects face using **MediaPipe Face Mesh**
3. Extracts facial landmarks (eyes & mouth)
4. Computes:

   * **EAR (Eye Aspect Ratio)** → detects eye closure
   * **MAR (Mouth Aspect Ratio)** → detects yawning
5. Applies threshold + frame stability logic
6. Triggers alert if drowsiness persists

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **OpenCV**
* **MediaPipe**
* **NumPy / SciPy**
* **HTML / CSS / JavaScript**

---

## 📂 Project Structure

```
Driver-Drowsiness-Monitoring-System/
│── app.py
│── detector.py
│── config.py
│── logger.py
│── requirements.txt
│── README.md
│
├── static/
│   ├── style.css
│   ├── app.js
│   └── alarm.wav
│
├── templates/
│   └── index.html
│
├── logs/
│   └── events.csv
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/programmer-suraj/Driver-Drowsiness-Monitoring-System.git
cd Driver-Drowsiness-Monitoring-System
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```bash
python app.py
```

---

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## ⚙️ Configuration

Edit `config.py` to tune detection:

```python
EYE_THRESH = 0.21
MOUTH_THRESH = 0.75
DROWSY_FRAMES = 20
```

---

## 📊 Output

* Real-time video with EAR & MAR values
* Status indicator:

  * ✅ Active
  * ⚠️ Drowsy
* CSV logs stored in `/logs/events.csv`

---

## 🔊 Audio Credits

Alarm sound from [https://pixabay.com/sound-effects/]
Free for use (no attribution required)

---

## 🚀 Future Improvements

* 👤 Head pose detection (attention tracking)
* 📱 Mobile notification alerts
* 📊 Advanced analytics dashboard
* 🧠 AI-based fatigue scoring system
* ☁️ Cloud logging & monitoring

---

## 🎯 Applications

* Driver safety systems
* Smart vehicles
* Fleet monitoring
* Industrial safety monitoring

---

## 👨‍💻 Author

Suraj Chouhan

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
