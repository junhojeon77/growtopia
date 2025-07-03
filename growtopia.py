import pyautogui
import time
import keyboard

print("Starting in 5 seconds... Switch to Growtopia.")
time.sleep(5)
start_time = time.time()
timeout = 3600  # 1 hour


while True:
    # Exit check first
    if keyboard.is_pressed('q'):
        print("Exiting early.")
        break

    if time.time() - start_time >= timeout:
        print("1 hour passed. Exiting.")
        break

    # Get current mouse position
    start_x, start_y = pyautogui.position()

    # PLACE first block
    pyautogui.click(button='left')
    time.sleep(0.3)

    # PLACE seconad block to the right
    pyautogui.moveTo(start_x - 50, start_y)
    pyautogui.click(button='left')
    time.sleep(0.3)
    
    pyautogui.press('a')

    # BREAK both blocks (longer break time)
    pyautogui.moveTo(start_x, start_y)
    pyautogui.keyDown('ctrl')
    time.sleep(1.4)  # longer punch for first block
    pyautogui.keyUp('ctrl')
    
    pyautogui.keyDown('a')
    time.sleep(0.3)# wait for the key to be held down
    pyautogui.keyUp('a')
    
    pyautogui.keyDown('d')
    time.sleep(0.8)  # wait for the key to be held down
    pyautogui.keyUp('d')
    
    pyautogui.press('a')

    
    # Move back to first block
    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.3)
