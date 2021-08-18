import phonenumbers
from time import timezone
from phonenumbers import carrier, geocoder
# --------------------------------------------------- Speak function --------------------------------------------------#
import pyttsx3  # voice setup

# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()
# --------------------------------------------------- Track number ----------------------------------------------------#

def track_number(inp):
    try:
        speak("Enter Mobile number with Country code")
        mobile_number = input("|+911234567890| Enter Here --:> ")
        mobile_number = phonenumbers.parse(mobile_number)
        print(timezone.time_zones_for_number(mobile_number))
        print("Service Provider : ", carrier.name_for_number(mobile_number, 'en'))
        print("Country : ", geocoder.description_for_number(mobile_number, 'en'))
        print("Valid Mobile number : ", phonenumbers.is_valid_number(mobile_number))
        print("Checking possibility of Number : ", phonenumbers.is_possible_number(mobile_number))
        return "Done"
    except:
        speak("make sure entered number is correct")