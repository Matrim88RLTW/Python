import time
import random
from pynput import mouse, keyboard

recording = False
recorded_positions = []

def on_press(key):
    global recording
    global recorded_positions
    if key == keyboard.Key.numpad1:
        if recording:
            # Stop recording
            recording = False
            print("Stopped recording")
        else:
            # Start recording
            recording = True
            print("Started recording")
    elif key == keyboard.Key.numpad6:
        # Stop the program
        return False

def on_click(x, y, button, pressed):
    global recording
    global recorded_positions
    if recording and button == mouse.Button.left and pressed:
        # Record the position of the mouse click
        recorded_positions.append((x, y))
        print("Recorded position:", (x, y))

# Set up the keyboard and mouse listeners
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

while True:
    if recorded_positions:
        print("Clicking recorded positions...")
        for position in recorded_positions:
            mouse_controller = mouse.Controller()
            mouse_controller.position = position
            time.sleep(random.uniform(1, 3))
            mouse_controller.click(mouse.Button.left)
        recorded_positions = []
    time.sleep(60)
