import csv
from datetime import datetime
import keyboard

# Define the CSV file to save the key press data
csv_file = 'key_presses.csv'

# Create and write the header of the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Key Name', 'Time Pressed'])

def on_press(event):
    # TODO remove it
    print(event)
    key_name = event.name
    time_pressed = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{key_name} pressed at {time_pressed}')

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([key_name, time_pressed])

# Hook the keyboard events
keyboard.on_press(on_press)

# Block forever, like listener.join()
# keyboard.wait('esc')
keyboard.wait()
