import csv
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "events.csv")


def ensure_log_file():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.isfile(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Time", "Status", "EAR", "MAR"])


def log_event(status, ear, mar):
    ensure_log_file()

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status,
            round(ear, 3),
            round(mar, 3)
        ])