import keyboard, subprocess, webbrowser, time
import sys, pyperclip  # read and get text from clipboard
from nltk.tokenize import sent_tokenize
# -----------------------------------------------------------------------------------------------------------
import asyncio # Multiprocessing 
# -----------------------------------------------------------------------------------------------------------


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


async def tab():
    try:
        keyboard.press_and_release('ctrl + t')
        speak("okay")
        speak("New and Fresh, Tab is ready.")
    except:
        speak("I am Unable, To Open New Tab for You")


async def sublime():
    try:
        subprocess.Popen("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
        speak("Sublime Text Editor is Opening...")
    except:
        speak(f"I am unable to open Sublime text editor. Please make a contact with Star")


async def vs_code():
    try:
        subprocess.Popen("C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        speak("Visual Studio is Opening...")
    except:
        speak(f"I am unable to open Visual studio code. Please make a contact with Star")


async def pycharm():
    try:
        subprocess.Popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe")
        speak("Pycharm is Opening...")
    except:
        speak(f"I am unable to open Pycharm IDE. Please make a contact with Star")


async def notepad():
    try:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        speak("NotePad is Opening...")
    except:
        speak(f"I am unable to open NotePad. Please make a contact with Star")


async def calculator():
    try:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        speak("Calculator is Opening...")
    except:
        speak(f"I am unable to open Calculator. Please make a contact with Star")


async def wordpad():
    try:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        speak("WordPad is Opening...")
    except:
        speak(f"I am unable to open WordPad. Please make a contact with Star")


async def browser():
    try:
        webbrowser.open("https://google.com")
        speak("Browser is Opening...")
    except:
        speak(f"I am unable to open Browser. Please make a contact with Star")


async def github():
    try:
        webbrowser.open("https://github.com/quickcodes")
        speak("Here is Quick Codes GitHub Repositery")
    except:
        speak(f"I am unable to open GitHub. Please make sure the path is correct")


async def youtube():
    try:
        webbrowser.open("https://youtube.com/")
        speak("Here is YouTube")

    except:
        speak(f"I am unable to open YouTube. Please make sure the path is correct")


async def spotify():
    try:
        webbrowser.open("https://spotify.com/")
        speak("Opening spotify")
    except:
        speak(f"I am unable to open spotify. Please make sure the path is correct")


async def twitter():
    try:
        webbrowser.open("https://twitter.com/")
        speak("Opening twitter")
    except:
        speak(f"I am unable to open twitter. Please make sure the path is correct")


async def instagram():
    try:
        webbrowser.open("https://instagram.com/")
        speak("Opening instagram")
    except:
        speak(f"I am unable to open instagram. Please make sure the path is correct")


async def google():
    try:
        webbrowser.open("https://google.com/")
        speak("Opening google")
    except:
        speak(f"I am unable to open google. Please make sure the path is correct")


async def amazon():
    try:
        webbrowser.open("https://amazon.com/")
        speak("Opening amazon")
    except:
        speak(f"I am unable to open amazon. Please make sure the path is correct")


async def flipkart():
    try:
        webbrowser.open("https://flipkart.com/")
        speak("Opening flipkart")
    except:
        speak(f"I am unable to open flipkart. Please make sure the path is correct")


async def linkedin():
    try:
        webbrowser.open("https://linkedin.com/")
        speak("Opening linkedin")
    except:
        speak(f"I am unable to open linkedin. Please make sure the path is correct")


async def select():
    time.sleep(2)
    keyboard.press_and_release('ctrl + a')
    speak("All text is selected")


async def copy():
    time.sleep(2)
    try:
        keyboard.press_and_release('ctrl + c')
        speak("Selected Text is Copied...")
    except:
        keyboard.press_and_release('ctrl + a')
        keyboard.press_and_release('ctrl + c')
        speak("okay")
        speak("All Text is Copied...")


async def paste():
    time.sleep(2)
    try:
        keyboard.press_and_release('ctrl + v')
        speak("Selected Text is Pasted...")
    except:
        speak("Your clipboard is empty")


async def cut():
    time.sleep(2)
    try:
        keyboard.press_and_release('ctrl + x')
        speak("Selected Text is Cut...")
    except:
        keyboard.press_and_release('ctrl + a')
        keyboard.press_and_release('ctrl + x')
        speak("okay")
        speak("All Text is Copied...")


async def read():
    time.sleep(2)
    try:
        keyboard.press_and_release('ctrl + c')
        keyboard.press_and_release('ctrl + c')
        if len(sys.argv) > 1:  # if file of text is more than a file it means it will return more than 1
            # Get address from command line.
            address = ' '.join(sys.argv[1:])
        else:
            # Get address from clipboard.
            address = pyperclip.paste()
        for sentence in sent_tokenize(address):
            speak(sentence)
    except:
        keyboard.press_and_release('ctrl + a')
        keyboard.press_and_release('ctrl + c')
        if len(sys.argv) > 1:  # if file of text is more than a file it means it will return more than 1
            # Get address from command line.
            address = ' '.join(sys.argv[1:])
        else:
            # Get address from clipboard.
            address = pyperclip.paste()
        for sentence in sent_tokenize(address):
            speak(sentence)
