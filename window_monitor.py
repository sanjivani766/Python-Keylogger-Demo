import time
from datetime import datetime
import pygetwindow as gw
import os

os.makedirs("logs", exist_ok=True)

def monitor_active_window():

    print("[INFO] Active window monitoring started")

    last_window = None

    while True:

        try:
            window = gw.getActiveWindow()

            if window:
                window_title = window.title

                if window_title != last_window:

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    log = f"{timestamp} [ACTIVE WINDOW] {window_title}"

                    print(log)

                    with open("logs/activity_log.txt", "a", encoding="utf-8") as f:
                        f.write(log + "\n")

                    last_window = window_title

        except:
            pass

        time.sleep(1)