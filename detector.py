import cv2
import numpy as np
import mediapipe as mp
from scipy.spatial import distance
from config import EYE_THRESH, MOUTH_THRESH


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]
MOUTH_IDX = [61, 291, 81, 178, 13, 14, 402, 311, 308, 324, 318, 78]


def euclidean(p1, p2):
    return distance.euclidean(p1, p2)


def eyeAspectRatio(eye):
    A = euclidean(eye[1], eye[5])
    B = euclidean(eye[2], eye[4])
    C = euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


def mouthAspectRatio(mouth):
    A = euclidean(mouth[2], mouth[10])
    B = euclidean(mouth[4], mouth[8])
    C = euclidean(mouth[0], mouth[6])
    return (A + B) / (2.0 * C)


def get_landmarks(face_landmarks, frame_shape, indices):
    h, w, _ = frame_shape
    return np.array([
        (int(face_landmarks.landmark[i].x * w),
         int(face_landmarks.landmark[i].y * h))
        for i in indices
    ])


def process_frame(frame):
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    output = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            leftEye = get_landmarks(face_landmarks, frame.shape, LEFT_EYE_IDX)
            rightEye = get_landmarks(face_landmarks, frame.shape, RIGHT_EYE_IDX)
            mouth = get_landmarks(face_landmarks, frame.shape, MOUTH_IDX)

            EAR = (eyeAspectRatio(leftEye) + eyeAspectRatio(rightEye)) / 2
            MAR = mouthAspectRatio(mouth)

            cv2.putText(frame, f"EAR: {round(EAR,3)}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            cv2.putText(frame, f"MAR: {round(MAR,3)}", (10, 85),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            output.append({
                "EAR": round(EAR, 3),
                "MAR": round(MAR, 3),
                "frame": frame
            })

    return output