from flask import Flask, render_template, Response, jsonify
import cv2
from detector import process_frame
from logger import log_event
from config import DROWSY_FRAMES, EYE_THRESH, MOUTH_THRESH
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

current_data = {
    "drowsy": False,
    "EAR": 0,
    "MAR": 0
}

frame_counter = 0


def generate_frames():
    global current_data, frame_counter

    while True:
        success, frame = camera.read()
        if not success:
            continue

        frame = cv2.resize(frame, (640, 400))

        results = process_frame(frame)

        if results:
            res = results[0]

            EAR = (current_data["EAR"] * 0.7) + (res["EAR"] * 0.3)
            MAR = res["MAR"]

            current_data["EAR"] = round(EAR, 3)
            current_data["MAR"] = round(MAR, 3)

            is_eye_closed = EAR < EYE_THRESH
            is_yawning = MAR > MOUTH_THRESH

            if is_eye_closed or is_yawning:
                frame_counter += 1
            else:
                frame_counter = 0

            if frame_counter >= DROWSY_FRAMES:
                if not current_data["drowsy"]:
                    log_event("DROWSY", EAR, MAR)
                current_data["drowsy"] = True
            else:
                current_data["drowsy"] = False

            frame = res["frame"]

            if current_data["drowsy"]:
                cv2.putText(frame, "DROWSY ALERT!", (350, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        ret, buffer = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               buffer.tobytes() + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/status')
def status():
    return jsonify(current_data)


if __name__ == "__main__":
    print("Open: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)