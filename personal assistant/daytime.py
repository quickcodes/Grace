from datetime import date
import time
import pyttsx3

# VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[5].id)  # total 14(0-13) voices are available


# SPEAK
def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()




@staticmethod
def tell_time():
    current_time = time.localtime()
    hour = int(time.strftime("%H", current_time))
    minute = int(time.strftime("%M", current_time))
    if hour < 12:
        print(f"\tIts {hour} : {minute} AM")
        speak(f"Its {hour} : {minute} AM")
    else:
        hour -= 12
        if hour == 0:
            hour = 12
        print(f"\tIts {hour} : {minute} PM")
        speak(f"Its {hour} : {minute} PM")

@staticmethod
def tell_dmy():
    today = date.today()
    print(today)
    month = today.strftime("%d %B , %Y")
    speak(f"Its {month}")
    day = today.strftime("%A")
    speak(f"And Ya Its {day}")
    print(f"And Ya Its {day}")

DayTime = type("DayTime", (), {
    "tell_time": tell_time,
    "tell_dmy": tell_dmy
})
