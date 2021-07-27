import keyboard, subprocess, webbrowser, os
import sys, pyperclip  # read and get text from clipboard
from nltk.tokenize import sent_tokenize
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

def tab():
    try:
        keyboard.press_and_release('ctrl + w')
        speak("okay")
        speak("Current tab is closed")
    except:
        speak("I am Unable, To Close Tab for You")


def sublime():
    try:
        os.system("TASKKILL /F /im sublime_text.exe")
        speak("Sublime Text Editor is Closed...")
    except:
        speak(f"I am unable to open Sublime text editor. Please make a contact with Star")


def vs_code():
    try:
        os.system("TASKKILL /F /im Code.exe")
        speak("Visual Studio is Closed...")
    except:
        speak(f"I am unable to open Visual studio code. Please make a contact with Star")


def pycharm():
    try:
        os.system("TASKKILL /F /im pycharm64.exe")
        speak("Pycharm is Opening...")
    except:
        speak(f"I am unable to open Pycharm IDE. Please make a contact with Star")


def notepad():
    try:
        os.system("TASKKILL /F /im notepad.exe")
        speak("NotePad is Opening...")
    except:
        speak(f"I am unable to open NotePad. Please make a contact with Star")


def calculator():
    try:
        os.system("TASKKILL /F /im calc.exe")
        speak("Calculator is Opening...")
    except:
        speak(f"I am unable to open Calculator. Please make a contact with Star")


def wordpad():
    try:
        os.system("TASKKILL /F /im write.exe")
        speak("WordPad is Opening...")
    except:
        speak(f"I am unable to open WordPad. Please make a contact with Star")


def browser():
    try:
        os.system("TASKKILL /F /im google.exe")
        speak("Browser is Opening...")
    except:
        speak(f"I am unable to open Browser. Please make a contact with Star")


def github():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def youtube():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def spotify():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def twitter():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def instagram():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def google():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def amazon():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def flipkart():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")


def linkedin():
    speak("Should I close, Current Tab?")
    lst = ["okay", "yes", "yup", "sure", "fine", "alright", "perfect", "do it"]
    ans = take_command().lower()
    for word in lst:
        if word in ans:
            try:
                keyboard.press_and_release('ctrl + w')
                speak("okay")
                speak("Current tab is closed")
            except:
                speak("I am Unable, To Close Tab for You")
        else:
            speak("Alright")

