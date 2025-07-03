import pyautogui
import time
import keyboard

print("Starting in 5 seconds... Switch to Growtopia and stand on the first block of the top row.")
time.sleep(5)

block_spacing = 0.05      # Time holding movement key per block (adjust if needed)
punch_time = 1.0          # Time spent punching each block
steps_per_row = 150       # Blocks per row (width)
pause_between_steps = 0.5 # Small delay between actions

def tap_key(key, duration=0.05):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

# Time tracker for ctrl reset
ctrl_hold_start = time.time()
ctrl_hold_max = 7.5  # seconds before resetting ctrl

try:
    current_row = 0
    pyautogui.keyDown('ctrl')  # Hold CTRL to punch blocks
    # Get current mouse position
    start_x, start_y = pyautogui.position()
    
    while True:
        # Reset CTRL hold if time exceeded
        if time.time() - ctrl_hold_start > ctrl_hold_max:
            pyautogui.keyUp('ctrl')
            time.sleep(0.5)
            pyautogui.keyDown('ctrl')
            ctrl_hold_start = time.time()

        # Move RIGHT and punch one row
        for step in range(steps_per_row):
            if keyboard.is_pressed('q'):
                raise KeyboardInterrupt

            # Reset CTRL hold if time exceeded inside the loop too
            if time.time() - ctrl_hold_start > ctrl_hold_max:
                pyautogui.keyUp('ctrl')
                time.sleep(0.5)
                pyautogui.keyDown('ctrl')
                ctrl_hold_start = time.time()

            tap_key('d', block_spacing)
            time.sleep(punch_time)

            time.sleep(0.3)

        pyautogui.keyUp('ctrl')  # Release CTRL after punching
       # break button down
        pyautogui.moveTo(start_x + 500, start_y + 200)

        # Repeated punching for 1 second
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.mouseUp(button='left')


        pyautogui.moveTo(start_x + 500, start_y)
        pyautogui.mouseDown(button='left')
        time.sleep(1)  # Hold for 1 second
        pyautogui.mouseUp(button='left')

        
        pyautogui.moveTo(start_x , start_y)
        
        pyautogui.keyDown('ctrl')  # Hold CTRL after punching

        # Move LEFT back across row
        for step in range(steps_per_row):
            if keyboard.is_pressed('q'):
                raise KeyboardInterrupt

            if time.time() - ctrl_hold_start > ctrl_hold_max:
                pyautogui.keyUp('ctrl')
                time.sleep(0.5)
                pyautogui.keyDown('ctrl')
                ctrl_hold_start = time.time()

            tap_key('a', block_spacing)
            time.sleep(punch_time)


        pyautogui.keyUp('ctrl')  # Release CTRL after punching

        # break button down
        pyautogui.moveTo(start_x - 500, start_y + 200)

        # Repeated punching for 1 second
        pyautogui.mouseDown(button='left')
        time.sleep(0.5)  # Hold for 1 second
        pyautogui.mouseUp(button='left')


        pyautogui.moveTo(start_x - 500, start_y)
        pyautogui.mouseDown(button='left')
        time.sleep(0.5)  # Hold for 1 second
        pyautogui.mouseUp(button='left')

        
        pyautogui.moveTo(start_x , start_y)

        pyautogui.keyUp('ctrl')  # Hold CTRL after punching

        current_row += 1
        print(f"Finished row {current_row}, moving to next row...")

except KeyboardInterrupt:
    pass

# pyautogui.keyUp('ctrl')
print("Stopped by user.")
