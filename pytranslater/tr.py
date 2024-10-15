import os
from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text

def detect_language(text):
    translator = Translator()
    detected_language = translator.detect(text).lang
    return detected_language

def print_language_options():
    print("Language Options:")
   
    print("English: en")
  
    print("German: de")
    print("Japanese: ja")
    print("Korean: ko")
    print("Hindi: hi")
    print("Telugu: te")

if __name__ == "__main__":

    str=input("Enter the text to translate: ")
    if str=='exit':
        exit()
    else:
        while True:
            text_to_translate = str

            print_language_options()

            dest_language = input("Enter the destination language code: ")

            # Translate the text
            translated_text = translate_text(text_to_translate, dest_language)
            print("Translated Text:", translated_text)

