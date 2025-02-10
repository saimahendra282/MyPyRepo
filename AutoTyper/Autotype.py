import pyautogui
import time
import random,pyttsx3

inp = """ 
Autotyping text goes here.......
"""

time.sleep(9)  # Delay to give you time to position your cursor

# Define a function to type with human-like speed
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # 5 is better cause it's an indian voice in my PC
    engine.setProperty('voice', voices[0].id)  # Index 1 represents a female voice
    engine.say(text)
    engine.runAndWait()
def type_human_like(text):

    for char in text:
        pyautogui.typewrite(char)
        # time.sleep(random.uniform(0.1, 0.3))

# Call the function with your input text
speak("auto typing started")
print("Autotyping..............")
type_human_like(inp)
speak("sir auto typing is completed so stop wasting time  and please have a look if it is correct or not")
# Press Enter to send the message
pyautogui.press("Enter")
