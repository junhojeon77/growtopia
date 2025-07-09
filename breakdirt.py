import pyautogui
import time
import keyboard

continue_break = True
print("Starting in 5 seconds... Switch to Growtopia and stand on the first block of the top row.")
time.sleep(5)

while continue_break:
    # Check if 'q' is pressed to quit
    if keyboard.is_pressed('q'):
        print("Exiting early.")
        pyautogui.mouseUp(button='left')  # Ensure mouse is released
        break

    # Hold left mouse button
    pyautogui.mouseDown(button='left')
    punch_start = time.time()

    while time.time() - punch_start < 7:
        if keyboard.is_pressed('q'):
            print("Exiting early.")
            pyautogui.mouseUp(button='left')
            continue_break = False
            break

        pyautogui.keyDown('d')
        time.sleep(0.05)
        pyautogui.keyUp('d')
        time.sleep(1.4)
        
    # Reset mouse click after 8 seconds
    pyautogui.mouseUp(button='left')
    time.sleep(1)  # brief pause
