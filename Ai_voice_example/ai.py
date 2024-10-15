# NO API NEEDED ONLY CODING
# COMMAND TO RUN python ai.py
# install these follwing pakages before copying my code.
# cv2
# pywhatkit
# pyttsx3
# speech_recognition
#code begins...................................................
import speech_recognition as sr
import webbrowser,subprocess
import pyttsx3,datetime
import os
import cv2
import pywhatkit as kit
#this function greets you when code started
def greet():
    print("Intiating.....")
    speak("Hello! I am Sunstromium, created by Sai Mahendra Studying CSE AT KL UNIVERSITY.")
    speak(" ")
    speak("you can ask me anything you want")
  
# it will makes your code speak
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # 5 is better
    engine.setProperty('voice', voices[0].id)  # Index 1 represents a female voice
    engine.say(text)
    engine.runAndWait()

#this function listen to what you are talking
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=20)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        speak("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        speak("Sorry, I could not understand your voice.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return None
  # our commands starts here
def execute_command(command): # to open websites 
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ["whatsapp", "https://web.whatsapp.com/"],
             ["telegram", "https://web.telegram.org/k/"]]
    for site in sites:

     if f"Open {site[0]}".lower() in command:
         speak(f"Opening {site[0]} sir...")
         webbrowser.open(site[1],new=2)
     if "what is the time now" in command or "what's the time now" in command:
         current_time = get_current_time()
         print("The current time is :",current_time)
         speak(f"The current time is {current_time}")
     elif "open youtube video about" in command:
         query = command.replace("open youtube video about", "").strip()
         kit.playonyt(query)
     elif "who coded you" in command:
        txt="I AM CODE BY SAI MAHENDRA BEJAWADA WHO IS STUDYING AT KL UNIVERSITY I AM VERY GRATEFULL TO HIM"
        speak(txt)
        print(txt)
    elif "search in google " in command: # command to search in google
        query = command.replace("search in google", "").strip()
        kit.search(query)
    elif "message" in command: # to send messege to whatsapp contact
        send_whatsapp_message()
    elif "flipkart" in command: # to search in flipkart
        query = command.replace("flipkart", "").strip()
        flipkart_search(query) 
    elif "give summary on topic" in command: # gives a summary about topic from wikepedia 
         query = command.replace("give summary on topic","").strip()
         kit.info(query, lines=3) # gives 3 lines summary from wikepedia
    elif "close" in command:
        print("Closing.....")
        speak("as you wish sir, exiting the code.")
        exit()  # Stop execution
   else:
    print("i am sorry i did not understand what you are speaking.")
    speak("i am sorry i did not understand what you are speaking.")

def send_whatsapp_message():
    speak("please enter your phone number here")
    print("(+91 u r number )")
    phone_number = input()
    message = input("enter the messege here")

    current_time = datetime.datetime.now()
    scheduled_time = current_time + datetime.timedelta(minutes=1, seconds=30)
    # it will send messege to person after 1 min it is activated
    kit.sendwhatmsg(phone_number, message, scheduled_time.hour, scheduled_time.minute)

def flipkart_search(query):
    speak(f"Searching Flipkart for {query}.")
    try:
        search_url = f"https://www.flipkart.com/search?q={query}"
        webbrowser.open(search_url, new=2)
    except Exception as e:
        speak(f"Error performing Flipkart search: {e}")


def main():
    greet()
    while True:
        user_input = listen()
        if user_input:
            execute_command(user_input)

if __name__ == "__main__":
    main()

# coding ends ...................................................................
# ⚠️ note: if you get any error regarding indexing or spaces it means i missed some spacing between snippets,adjust the spaces to run  
