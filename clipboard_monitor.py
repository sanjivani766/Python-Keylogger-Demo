import pyperclip
import time
import os

os.makedirs("logs", exist_ok=True)

def monitor_clipboard():

    last_data = ""

    print("[INFO] Clipboard monitor started")

    while True:

        data = pyperclip.paste()

        if data != last_data:

            with open("logs/activity_log.txt", "a", encoding="utf-8") as f:
                f.write(f"[Clipboard] {data}\n")

            if len(data) > 100:
                print("[INFO] Large clipboard content captured")
            else:
                print(f"[INFO] Clipboard captured: {data}")

            last_data = data

        time.sleep(5)