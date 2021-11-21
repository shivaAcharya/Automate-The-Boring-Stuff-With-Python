import pyautogui, time
time.sleep(5)
pyautogui.click() # Click to make the window active.
distance = 300
change = 20

while distance > 1:
    pyautogui.drag(distance, 0, duration=0.2) # Move Right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2) # Move Down
    pyautogui.drag(-distance, 0, duration=0.2) # Move Left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2) # Move Up
    