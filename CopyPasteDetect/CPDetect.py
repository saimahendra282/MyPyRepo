import time
import pyperclip
import keyboard

def detect_paste():
    last_clipboard_content = ""
    print("Monitoring clipboard and keyboard events for pasted content. Press Ctrl+C to stop.")

    try:
        while True:
            # Monitor clipboard changes
            current_clipboard_content = pyperclip.paste()

            # If the clipboard content changes, print the new content
            if current_clipboard_content != last_clipboard_content:
                print(f"Pasted Content Detected: {current_clipboard_content}")
                last_clipboard_content = current_clipboard_content

            # Detect Ctrl+V key press as paste operation
            if keyboard.is_pressed("ctrl") and keyboard.is_pressed("v"):
                print("Detected Ctrl+V (Paste)")

            # Wait briefly to reduce CPU usage
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopped monitoring clipboard and keyboard.")

if __name__ == "__main__":
    detect_paste()
