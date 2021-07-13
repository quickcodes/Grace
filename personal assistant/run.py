import pyttsx3  # voice setup
import speech_recognition as sr  # speech recognization
import os  # operating system

# BASIC AND IMPORTANT SETUP --------------------------------------------------------------------------------------------
# VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[1].id)  # total 15(0-14) voices are available
engine.setProperty('voices', 50)


# SPEAK
def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()


# VOICE RECOGNITION
def take_command():
    while True:
    # it will take input from microphone
    # and return string as a output
        r = sr.Recognizer()  # take input and store in variable
        with sr.Microphone() as source:
            print("\tListening...")
            r.pause_threshold = 1
            # r.energy_threshold = 400
            audio = r.listen(source)

        try:
            print("\tRecognizing...")
            query = r.recognize_google(audio, language='en-in')
            if 'grace' in query:
                speak("Hello... I'm here to make thing's easier than ever. "
                      "Just you need to ask")
                os.startfile("main.py")
        except Exception:
            print("\tListening again...")


# take_command()
speak('Hello star i am your personal assistant how are you')
