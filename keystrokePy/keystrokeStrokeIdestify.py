import keyboard

print("Keylogger started. Press ESC to stop.")

def log_key(key_event):
    # Log key pressed to the console
    print(f"Key Pressed: {key_event.name}")

# Register callback for all key events
keyboard.on_press(log_key)

# Block until ESC key is pressed to exit
keyboard.wait('esc')

print("Keylogger stopped.")
