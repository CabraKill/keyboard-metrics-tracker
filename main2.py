import csv
from datetime import datetime
from pynput import keyboard

# Define the CSV file to save the key press data
csv_file = 'key_presses.csv'

# Create and write the header of the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Key Name', 'Key Code', 'Time Pressed'])

def on_press(key):
    try:
        key_name = key.char
        key_code = key.vk
    except AttributeError:
        key_name = str(key)
        key_code = key.value.vk

    time_pressed = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([key_name, key_code, time_pressed])

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()

# while True:
#     pass
