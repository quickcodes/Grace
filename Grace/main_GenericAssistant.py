from neuralintents import GenericAssistant
import play, time, requests, webbrowser
import wikipedia, pywhatkit as pwk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import pyttsx3  # voice setup

#
# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[6].id)


def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()




class AssistantNew(GenericAssistant):
    def request(self, message):
        ints = self._predict_class(message)
        # print("Prediction : ", ints)
        if float(ints[0]['probability']) > 0.85:
            if ints[0]['intent'] in self.intent_methods.keys():
                msg = self.intent_methods[ints[0]['intent']](message)
                print(msg)
            else:
                # print(self._get_response(ints, self.intents))
                ans = (self._get_response(ints, self.intents))
                print("Answer : ", end=" ")
                print(ans)
                speak(ans)
        else:
            print("I have something related this please type 'yes'")
            speak("I have something related this please type 'yes'")
            ask = input("You : ").lower()
            if 'yes' in ask:
                wiki(message)
            else:
                print("Grace :  Okay")
                speak("Okay")
            # lst = ['ok', 'sure', 'definitely', 'yup', "yep", "respectable", "of course", "green light", "confirm",
            #        "okeydokey", "surely", "satisfactory", "tolerable", "correct", "good", "not bad",
            #        "up to scratch",
            #        "accurate", "no problem", "alright", "yes", "Here we go", "sounds good", "alright then",
            #        "absolutely",
            #        "as you say"]
            # print("point 1")
            # for letter in lst:
            #     if letter in ask:
            #         print("searching.....")
            #         words = word_tokenize(message)
            #         res = [w for w in words if not w in stopwords ]
            #         wiki(res)

class User:  # USER CLASS
    name = "Star"
    location = "Indore"

    def __init__(self, location="Indore"):
        self.location = location

    def set_name(self, query):
        query.replace("my", "")
        query.replace("name", "")
        query.replace("is", "")
        self.name = query
        print(f"Got it Your name is {self.name}")

    def set_location(self, location):
        self.location = location


user = User()

import open_software, close_software
import re
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def by(inp):
    speak("byby")
    exit()


def tell_time(inp):
    current_time = time.localtime()
    hour = int(time.strftime("%H", current_time))
    minute = int(time.strftime("%M", current_time))
    if hour < 12:
        return f"Its {hour} : {minute} AM"
    else:
        hour -= 12
        if hour == 0:
            hour = 12
        return f"Its {hour} : {minute} PM"


def tell_joke(inp):
    json_data = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    first_line = json_data['setup']
    punch_line = json_data['punchline']
    # print(first_line)
    # time.sleep(2)
    # print(punch_line)
    return "Here is the joke" + "\n" + str(first_line) + "\n" + str(punch_line)


def wiki(inp):
    inp = inp.replace("tell", "").replace("me", "").replace("about", "").replace("who", "").replace("is", "")
    inp = inp.replace("what", "").replace("are", "").replace("someting", "").replace("of", "").replace("know", "")
    inp = inp.replace("kaun h", "").replace("baare m", "").replace("batao", "").replace("of", "").replace("know", "")
    inp = inp.replace("give me details", "").replace("jankari do", "").replace("collect information", "").replace(
        "pata lagao", "")
    inp = inp.replace("search", "")  # .replace("details","").replace("kaun","").replace("","").replace("know","")
    try:
        result = wikipedia.summary(inp, sentences=1)
        return result
    except:
        pwk.search(inp)
        return "Here we go!..."


def show_meme(inp):
    json_data = requests.get("https://meme-api.herokuapp.com/gimme").json()
    meme_url = json_data["url"]
    webbrowser.open(meme_url)
    return "Yup!"


def daily(inp):
    play.PlaySongs.daily()
    return "Here we go!..."


def international(inp):
    play.PlaySongs.international()
    return "Here we go!..."


# ---------------------------------------------------- Open Things -----------------------------------------------------#

def open_tab(inp):
    speak("Okay")
    open_software.tab()
    return "Task Completed!"


def open_sublime(inp):
    speak("Okay")
    open_software.sublime()
    return "Task Completed!"


def open_vs_code(inp):
    speak("Okay")
    open_software.vs_code()
    return "Task Completed!"


def open_pycharm(inp):
    speak("Okay")
    open_software.pycharm()
    return "Task Completed!"


def open_notepad(inp):
    speak("Okay")
    open_software.notepad()
    return "Task Completed!"


def open_calculator(inp):
    speak("Okay")
    open_software.calculator()
    return "Task Completed!"


def open_wordpad(inp):
    speak("Okay")
    open_software.wordpad()
    return "Task Completed!"


def open_browser(inp):
    speak("Okay")
    open_software.browser()
    return "Task Completed!"


def open_github(inp):
    speak("Okay")
    open_software.github()
    return "Task Completed!"


def open_spotify(inp):
    speak("Okay")
    open_software.spotify()
    return "Task Completed!"


def open_twitter(inp):
    speak("Okay")
    open_software.twitter()
    return "Task Completed!"


def open_instagram(inp):
    speak("Okay")
    open_software.instagram()
    return "Task Completed!"


def open_google(inp):
    speak("Okay")
    open_software.google()
    return "Task Completed!"


def open_amazon(inp):
    speak("Okay")
    open_software.amazon()
    return "Task Completed!"


def open_flipkart(inp):
    speak("Okay")
    open_software.flipkart()
    return "Task Completed!"


def open_linkedin(inp):
    speak("Okay")
    open_software.linkedin()
    return "Task Completed!"


# ---------------------------------------------------- Close Things -----------------------------------------------------#

def close_tab(inp):
    speak("Okay")
    close_software.tab()
    return "Task Completed!"


def close_sublime(inp):
    speak("Okay")
    close_software.sublime()
    return "Task Completed!"


def close_vs_code(inp):
    speak("Okay")
    close_software.vs_code()
    return "Task Completed!"


def close_pycharm(inp):
    speak("Okay")
    close_software.pycharm()
    return "Task Completed!"


def close_notepad(inp):
    speak("Okay")
    close_software.notepad()
    return "Task Completed!"


def close_calculator(inp):
    speak("Okay")
    close_software.calculator()
    return "Task Completed!"


def close_wordpad(inp):
    speak("Okay")
    close_software.wordpad()
    return "Task Completed!"


def close_browser(inp):
    speak("Okay")
    close_software.browser()
    return "Task Completed!"


def close_github(inp):
    speak("Okay")
    close_software.github()
    return "Task Completed!"


def close_spotify(inp):
    speak("Okay")
    close_software.spotify()
    return "Task Completed!"


def close_twitter(inp):
    speak("Okay")
    close_software.twitter()
    return "Task Completed!"


def close_instagram(inp):
    speak("Okay")
    close_software.instagram()
    return "Task Completed!"


def close_google(inp):
    speak("Okay")
    close_software.google()
    return "Task Completed!"


def close_amazon(inp):
    speak("Okay")
    close_software.amazon()
    return "Task Completed!"


def close_flipkart(inp):
    speak("Okay")
    close_software.flipkart()
    return "Task Completed!"


def close_linkedin(inp):
    close_software.linkedin()
    return "Task Completed!"


# ---------------------------------------------------- Clipboard -----------------------------------------------------#


def select(inp):
    speak("Okay")
    open_software.select()
    return "Task Completed!"


def copy(inp):
    speak("Okay")
    open_software.copy()
    return "Task Completed!"


def cut(inp):
    speak("Okay")
    open_software.cut()
    return "Task Completed!"


def read(inp):
    speak("Okay")
    open_software.read()
    return "Task Completed!"


# ---------------------------------------------------- Mathemetics -----------------------------------------------------#

def add(inp):
    try:
        numbers = re.findall('\d+', inp)
        sum = 0
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        for number in numbers:
            sum += number
        return "Its " + str(sum)
    except:
        return "Something went wrong."


def sub(inp):
    try:
        numbers = re.findall('\d+', inp)
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])

        ans = numbers[0]
        num = 0
        # print(numbers)
        # print("answer: ", ans)

        while num < (len(numbers) - 1):
            ans -= numbers[num + 1]
            num += 1

        return "Its " + str(ans)
    except:
        return "Something went wrong."


def mul(inp):
    try:
        numbers = re.findall('\d+', inp)
        mul = 1
        for number in numbers:
            mul *= int(number)
        return "Its " + str(mul)
    except:
        return "Something went wrong."


def power(inp):
    try:
        numbers = re.findall('\d+', inp)

        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])

        ans = numbers[0]
        num = 0

        if len(numbers) == 1:
            ans = numbers[0] * numbers[0]
        else:
            while num < (len(numbers) - 1):
                print("Current ans : ", ans)
                ans **= numbers[num + 1]
                num += 1

        return "Its : " + str(ans)
    except:
        return "Something went wrong."


def div(inp):
    try:
        numbers = re.findall('\d+', inp)
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        ans = numbers[0] / numbers[1]
        return "Its " + str(ans)
    except:
        return "Something went wrong"


# --------------------------------------------------- Track number ----------------------------------------------------#

def track_number(inp):
    speak("Enter Mobile number with Country code")
    mobile_number = input("|+911234567890| Enter Here --:> ")
    mobile_number = phonenumbers.parse(mobile_number)
    print(timezone.time_zones_for_number(mobile_number))
    print("Service Provider : " , carrier.name_for_number(mobile_number, 'en'))
    print("Country : " , geocoder.description_for_number(mobile_number, 'en'))
    print("Valid Mobile number : " , phonenumbers.is_valid_number(mobile_number))
    print("Checking possibility of Number : " , phonenumbers.is_possible_number(mobile_number))
    return "Done"

# ----------------------------------------------------- Mapping -------------------------------------------------------#
mapping = {
    "time": tell_time,
    "joke": tell_joke,
    "exit": by,
    "meme": show_meme,
    'wiki': wiki,
    'international': international,
    'daily': daily,

    "open_tab": open_tab,
    "open_sublime": open_sublime,
    "open_vs_code": open_vs_code,
    "open_pycharm": open_pycharm,
    "open_notepad": open_notepad,
    "open_calculator": open_calculator,
    "open_wordpad": open_wordpad,
    "open_browser": open_browser,
    "open_github": open_github,
    "open_spotify": open_spotify,
    "open_twitter": open_twitter,
    "open_instagram": open_instagram,
    "open_amazon": open_amazon,
    "open_flipkart": open_flipkart,
    "open_linkedin": open_linkedin,

    "close_tab": close_tab,
    "close_sublime": close_sublime,
    "close_vs_code": close_vs_code,
    "close_pycharm": close_pycharm,
    "close_notepad": close_notepad,
    "close_calculator": close_calculator,
    "close_wordpad": close_wordpad,
    "close_browser": close_browser,
    "close_github": close_github,
    "close_spotify": close_spotify,
    "close_twitter": close_twitter,
    "close_instagram": close_instagram,
    "close_amazon": close_amazon,
    "close_flipkart": close_flipkart,
    "close_linkedin": close_linkedin,

    "select": select,
    "copy": copy,
    "cut": cut,
    "read": read,

    "add": add,
    "sub": sub,
    "mul": mul,
    "power": power,
    "div": div,

    "track_number": track_number
}

assistant = AssistantNew("intents.json", mapping)

# assistant.train_model()
# assistant.save_model()
assistant.load_model()

while True:
    messge = input("You : ")
    for sentence in sent_tokenize(messge):
        # print('you said: ', sentence)
        print("Grace : ", end=" ")
        assistant.request(sentence)
