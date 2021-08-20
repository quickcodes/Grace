# --------------------------------------------------- Speak function --------------------------------------------------#
import pyttsx3  # voice setup

# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[6].id)


def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()

