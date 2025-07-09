import pyautogui
import time
import keyboard
import random
import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import pygetwindow as gw
import json

# Setup tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/junho/Tesseract-OCR/tesseract.exe"

def check_and_drop_if_200(start_x, start_y):
    save_dir = os.path.expanduser(r"screenshots")
    os.makedirs(save_dir, exist_ok=True)

    # Approximate location of the item count
    item_x = start_x + 10
    item_y = start_y + 470
    count_region = (item_x, item_y, 100, 50)  # Smaller height to avoid the line above

    # Take screenshot of item count
    screenshot = pyautogui.screenshot(region=count_region)

    # Convert to grayscale
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Binarize to black/white
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    kernel = np.ones((1, 2), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)


    # Optional: crop the inner area more tightly to eliminate box lines
    h, w = img.shape
    img = imgimg = img[5:h-5, 5:w-20]  # aggressive crop on right side
  # trim borders

    # Resize to improve OCR accuracy
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # OCR configa
    config = r'--psm 7 -c tessedit_char_whitelist=0123456789'

    # OCR Read
    text = pytesseract.image_to_string(img, config=config).strip()
    cv2.imwrite(os.path.join(save_dir, "processed.png"), img)
    print(f"[OCR] Detected text: '{text}'")

    try:
        count = int(''.join(filter(str.isdigit, text)))
        if count == 200:
            print("✅ Detected 200 items! Initiating drop sequence.")
            pyautogui.moveTo(item_x, item_y)
            pyautogui.keyDown('a')
            time.sleep(0.8)
            pyautogui.keyUp('a')
            pyautogui.moveTo(item_x, item_y)
            pyautogui.click()
            time.sleep(0.2)

            drop_x = item_x + 650
            drop_y = item_y + 120
            pyautogui.moveTo(drop_x, drop_y)
            pyautogui.click()
            time.sleep(1.5)
            pyautogui.press('enter')
            print("✅ Drop sequence completed.")
            # Wait a bit before next check
            time.sleep(2)
            
            pyautogui.keyDown('d')
            time.sleep(1.5)
            pyautogui.keyUp('d')
        
            
            pyautogui.moveTo(item_x - 50, item_y)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(1)
        else:
            print(f"[INFO] Current count: {count}. Not 200, continuing.")
    except ValueError:
        print("[WARN] OCR failed to parse number.")


print("Starting in 5 seconds... Move your mouse to the black circle.")
time.sleep(5)
start_time = time.time()
duration = 8000

position_file = "position.json"

window = gw.getWindowsWithTitle("Growtopia")[0]

if not window:
    print('Error growtopia not found')
    exit()

win_left, win_top = window.left, window.top
win_width, win_height = window.width, window.height

if os.path.exists(position_file):
    with open(position_file, "r") as f:
        data = json.load(f)
        percent_x = data["percent_x"]
        percent_y = data["percent_y"]
        print(f"[INFO] Loaded saved relative position: ({percent_x*100:.1f}%, {percent_y*100:.1f}%)")
else:
    # Get mouse absolute position
    mouse_x, mouse_y = pyautogui.position()

    # Calculate relative percentage position inside window
    percent_x = (mouse_x - win_left) / win_width
    percent_y = (mouse_y - win_top) / win_height

    # Save it
    with open(position_file, "w") as f:
        json.dump({"percent_x": percent_x, "percent_y": percent_y}, f)
    print(f"[INFO] Saved relative position: ({percent_x*100:.1f}%, {percent_y*100:.1f}%)")


start_x = int(window.left + window.width * percent_x)
start_y = int(window.top + window.height * percent_y)


while True:
    # ✅ Check for 200 count and drop
    check_and_drop_if_200(start_x, start_y)
    
    if keyboard.is_pressed('q') or (time.time() - start_time > duration):
        print("⏹️ Exiting early.")
        break
        
    switch = random.randint(1, 2)


    if switch == 1:
        pyautogui.click(button='left')
        time.sleep(0.3)

        pyautogui.moveTo(start_x - 50, start_y)
        pyautogui.click(button='left')
        time.sleep(0.3)

        pyautogui.press('a')

    elif switch == 2:
        pyautogui.moveTo(start_x - 50, start_y)
        pyautogui.click(button='left')
        time.sleep(0.3)

        pyautogui.moveTo(start_x, start_y)
        pyautogui.click(button='left')
        time.sleep(0.3)

        pyautogui.press('a')

    # Breaking
    pyautogui.moveTo(start_x, start_y)
    pyautogui.keyDown('ctrl')
    time.sleep(1.4)
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('a')
    time.sleep(0.35)
    pyautogui.keyUp('a')

    pyautogui.keyDown('d')
    time.sleep(0.8)
    pyautogui.keyUp('d')

    pyautogui.press('a')
    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.3)


