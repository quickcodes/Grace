import keyboard, subprocess, webbrowser, os
import sys, pyperclip  # read and get text from clipboard
from nltk.tokenize import sent_tokenize
# -----------------------------------------------------------------------------------------------------------
import asyncio # Multiprocessing 
# -----------------------------------------------------------------------------------------------------------

import speech_recognition as sr
# --------------------------------------------------- Speak function --------------------------------------------------#

import pyttsx3  # voice setup

#
# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[6].id)


def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()

# VOICE RECOGNITION
def take_command():
    # it will take input from microphone
    # and return string as a output
    r = sr.Recognizer()  # take input and store in variable
    with sr.Microphone() as source:
        # print("\tListening...")
        speak("I'm, Listening")
        r.pause_threshold = 0.5
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        # print("\tRecognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # print(f"\tYou said: {query}\n\t")
        # speak("okay")
    except Exception:
        print("\tPlease say that again...")
        return "\tNone"
    return query

async def tab():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
                return
            except:
                speak("I am Unable, To Close Tab for You")
                return
        else:
            speak("Alright")
            return


async def sublime():
    try:
        os.system("TASKKILL /F /im sublime_text.exe")
        speak("Sublime Text Editor is Closed...")
    except:
        speak(f"I am unable to close Sublime text editor. Please make a contact with Star")


async def vs_code():
    try:
        os.system("TASKKILL /F /im Code.exe")
        speak("Visual Studio is Closed...")
    except:
        speak(f"I am unable to close Visual studio code. Please make a contact with Star")


async def pycharm():
    try:
        os.system("TASKKILL /F /im pycharm64.exe")
        speak("Pycharm is closed...")
    except:
        speak(f"I am unable to close Pycharm IDE. Please make a contact with Star")


async def notepad():
    try:
        os.system("TASKKILL /F /im notepad.exe")
        speak("NotePad is closed...")
    except:
        speak(f"I am unable to close NotePad. Please make a contact with Star")


async def calculator():
    try:
        os.system("TASKKILL /F /im calc.exe")
        speak("Calculator is closed...")
    except:
        speak(f"I am unable to close Calculator. Please make a contact with Star")


async def wordpad():
    try:
        os.system("TASKKILL /F /im write.exe")
        speak("WordPad is closed...")
    except:
        speak(f"I am unable to close WordPad. Please make a contact with Star")


async def browser():
    try:
        os.system("TASKKILL /F /im google.exe")
        speak("Browser is closed...")
    except:
        speak(f"I am unable to close Browser. Please make a contact with Star")


# async def github():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def youtube():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def spotify():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def twitter():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def instagram():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def google():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def amazon():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def flipkart():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")
#
#
# async def linkedin():
#     speak("Should I close, Current Tab?")
#     lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
#     ans = take_command().lower()
#     for word in lst:
#         if word in ans:
#             try:
#                 keyboard.press_and_release('ctrl + w')
#                 speak("okay")
#                 speak("Current tab is closed")
#             except:
#                 speak("I am Unable, To Close Tab for You")
#         else:
#             speak("Alright")

