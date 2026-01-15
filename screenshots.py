import time
import mss
import numpy as np
import cv2

SAVE_PATH = "screenshots"
INTERVAL = 3  # Seconds

with mss.mss() as sct:
    monitor = sct.monitors[2]  # Change this index based on the output

    while True:
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        filename = f"{SAVE_PATH}screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, img)
        print(f"Saved {filename}")

        time.sleep(INTERVAL)
