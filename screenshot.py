import pyautogui
import time
from datetime import datetime
import os

os.makedirs("screenshots", exist_ok=True)

def capture_screenshot():

    print("[INFO] Screenshot capture started")

    while True:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/screen_{timestamp}.png"

        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

        print(f"[INFO] Screenshot saved: {filename}")

        time.sleep(30)