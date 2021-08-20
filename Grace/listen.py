# ------------------------------------------------- Voice Recognization -----------------------------------------------#
import speech_recognition as sr


# VOICE RECOGNITION
def take_command():
    # it will take input from microphone
    # and return string as a output
    r = sr.Recognizer()  # take input and store in variable
    with sr.Microphone() as source:
        print("---------------Listening---------------")
        r.pause_threshold = 0.5
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("---------------Recognizing---------------")
        query = r.recognize_google(audio, language='en-in')
        # print(f"\tYou said: {query}\n\t")
        # speak("okay")
    except Exception:
        print("---------------Please say that again---------------")
        return "None"
    return query
