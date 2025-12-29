import cv2
import csv
import os
import time
from datetime import datetime
from ultralytics import YOLO

print("Smart Exam Cheating Detection System Started")

# =========================
# SETUP DIRECTORIES
# =========================
os.makedirs("logs", exist_ok=True)
os.makedirs("evidence", exist_ok=True)

# =========================
# SETUP LOG FILE
# =========================
log_path = "logs/cheating_log.csv"
file_exists = os.path.isfile(log_path)

log_file = open(log_path, "a", newline="")
log_writer = csv.writer(log_file)

if not file_exists:
    log_writer.writerow(["Time", "Event", "Cheating Score", "Evidence"])

# =========================
# LOAD MODELS
# =========================
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# YOLOv8 model
yolo_model = YOLO("yolov8n.pt")

# =========================
# CHEATING SCORE FUNCTION
# =========================
def calculate_cheating_score(face_count, phone_detected):
    score = 0
    if face_count == 0:
        score += 40
    elif face_count > 1:
        score += 50
    if phone_detected:
        score += 60
    return min(score, 100)

# =========================
# SCREENSHOT COOLDOWN
# =========================
last_capture_time = 0
COOLDOWN_SECONDS = 5

# =========================
# MAIN LOOP
# =========================
while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    phone_detected = False

    # ---------- FACE DETECTION ----------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_count = len(faces)

    status = "NORMAL"
    if face_count == 0:
        status = "NO_FACE_DETECTED"
    elif face_count > 1:
        status = "MULTIPLE_FACES"

    # ---------- PHONE DETECTION (YOLO) ----------
    results = yolo_model(frame, conf=0.5, verbose=False)
    for result in results:
        for box in result.boxes:
            label = yolo_model.names[int(box.cls[0])]
            if label == "cell phone":
                phone_detected = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(
                    frame,
                    "PHONE DETECTED",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

    # ---------- CHEATING SCORE ----------
    cheating_score = calculate_cheating_score(face_count, phone_detected)

    # ---------- AUTO SCREENSHOT + LOG ----------
    current_time = time.time()
    if cheating_score >= 60 and (current_time - last_capture_time) > COOLDOWN_SECONDS:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # ✅ FINAL FIX YOU ASKED FOR
        event_name = status
        if phone_detected:
            event_name = "PHONE_DETECTED"

        screenshot_name = f"evidence/{timestamp}_{event_name}.jpg"
        cv2.imwrite(screenshot_name, frame)

        log_writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            event_name,
            cheating_score,
            screenshot_name
        ])

        last_capture_time = current_time

    # ---------- DRAW FACE BOXES ----------
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # ---------- DISPLAY ----------
    cv2.putText(
        frame,
        f"Status: {event_name if cheating_score >= 60 else status}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255) if cheating_score >= 60 else (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Faces: {face_count}",
        (10, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Cheating Confidence: {cheating_score}%",
        (10, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 255) if cheating_score >= 60 else (0, 255, 0),
        2
    )

    cv2.imshow("Smart Exam Cheating Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =========================
# CLEANUP
# =========================
cap.release()
log_file.close()
cv2.destroyAllWindows()
print("System stopped safely")
