import nltk
import wikipedia.wikipedia
from nltk.stem.lancaster import LancasterStemmer

steammer = LancasterStemmer()

import numpy
import tflearn
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
import random
import json
import pickle


# User Class
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

with open("intents.json") as file:
    data = json.load(file)
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    # Training of model
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent['tag'])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    words = [steammer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [steammer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tf.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# comment - try, model.load, and except line to train model
try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


# ------------------------------------------------------------------------------------------------------

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [steammer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = (1)

    return numpy.array(bag)


# ----------------------------------------------------- Main Work -----------------------------------------------------#
# ------------------------------------------------- Starting from here ------------------------------------------------#


import time, requests, webbrowser, play, speech_recognition as sr
import pywhatkit as pwk
from nltk.tokenize import sent_tokenize, word_tokenize
import open_software, close_software, password_crack
import re
from functools import reduce
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

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


# ------------------------------------------------- Voice Recognization -----------------------------------------------#

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


# ----------------------------------------------------- Functions ------------------------------------------------------#

def by(inp):
    print("bye bye")
    print("You can call me any time by saying my Name like, Hello Grace")
    time.sleep(2)
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


def password(inp):
    speak("Lets me Guess the Password")
    speak("Please enter the complexity of Password")
    password_crack.main()
    return "Hopefully you Enjoyed it."


# many other methods are also availabe in paly file
def daily(inp):
    play.PlaySongs.daily()
    play.youtube_auto()  # for full screen mode
    return "Here we go!..."


def international(inp):
    play.PlaySongs.international()
    play.youtube_auto()  # for full screen mode
    return "Here we go!..."


# --------------------------------------------------- Api Functions ----------------------------------------------------#

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


def temperature(inp):
    city = "indore"
    api = "http://api.openweathermap.org/data/2.5/weather?q= " + city + " &appid=17a1bc1a00e0510bfada3baeb2e4dd98"
    json_data = requests.get(api).json()
    climate = json_data['weather'][0]['main']
    # climate_des = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    weather2 = "The temperature is " + str(temp) + "° Celsius "
    return weather2


def weather(inp):
    city = "indore"
    api = "http://api.openweathermap.org/data/2.5/weather?q= " + city + " &appid=17a1bc1a00e0510bfada3baeb2e4dd98"
    json_data = requests.get(api).json()
    climate = json_data['weather'][0]['main']
    # climate_des = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    country = json_data['sys']['country']
    sunrise = time.strftime('in the morning  At %I  %M AM.', time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunset = time.strftime('Happening At %I  %M PM.', time.gmtime(json_data['sys']['sunset'] - 19800))

    weather1 = " Today you see" + climate + " In the sky.. "
    weather2 = " And the temperature is probably " + str(temp) + "° Celsius "
    weather3 = " The Minimum Temperature you notice is " + str(min_temp) + " And. The Maximum you get is " + str(
        max_temp)
    weather4 = f" In Our city Air is going. At the speed of " + str(wind_speed) + " Kilometer PerHour "
    weather5 = " I Notice that. Today Sunrises " + str(sunrise) + " And goes down mean Sunset is almost " + str(sunset)
    weather6 = " And the Pressure is in the Air is " + str(pressure) + " Or Humidity in the atmosphere is " + str(
        humidity) + "%"
    weather7 = " Hopefully you enjoying your day. "

    speak(weather1)
    speak(weather2)
    speak(weather3)
    speak(weather4)
    speak(weather5)
    speak(weather6)
    speak(weather7)
    return "All Done!"


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


# ---------------------------------------------------- Clipboard -----------------------------------------------------#


def select(inp):
    speak("Okay")
    open_software.select()
    return "Task Completed!"


def copy(inp):
    speak("Okay")
    open_software.copy()
    return "Task Completed!"


def paste(inp):
    speak("Okay")
    open_software.paste()
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
    # ------ GENERAL APPROACH ----------------#
    #     try:
    #         numbers = re.findall('\d+', inp)
    #         sum = 0
    #         for i in range(0, len(numbers)):
    #             numbers[i] = int(numbers[i])
    #         for number in numbers:
    #             sum += number
    #         return "Its " + str(sum)
    #     except:
    #         return "Something went wrong."
    # ------ MODERN APPROACH ----------------#
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x + y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


def sub(inp):
    # ------ GENERAL APPROACH ----------------#
    # try:
    #     numbers = re.findall('\d+', inp)
    #     for i in range(0, len(numbers)):
    #         numbers[i] = int(numbers[i])
    #
    #     ans = numbers[0]
    #     num = 0
    #     print(numbers)
    #     print("answer: ", ans)
    #
    #     while num < (len(numbers) - 1):
    #         ans -= numbers[num + 1]
    #         num += 1
    #
    #     return "Its " + str(ans)
    # except:
    #     return "Something went wrong."
    # ------ MODERN APPROACH ----------------#
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x - y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


def mul(inp):
    # ------ GENERAL APPROACH ----------------#
    # try:
    #     numbers = re.findall('\d+', inp)
    #     mul = 1
    #     for number in numbers:
    #         mul *= int(number)
    #     return "Its " + str(mul)
    # except:
    #     return "Something went wrong."
    # ------ MODERN APPROACH ----------------#
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x * y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


def power(inp):
    # ------ GENERAL APPROACH ----------------#
    # try:
    #     numbers = re.findall('\d+', inp)
    #
    #     for i in range(0, len(numbers)):
    #         numbers[i] = int(numbers[i])
    #
    #     ans = numbers[0]
    #     num = 0
    #
    #     if len(numbers) == 1:
    #         ans = numbers[0] * numbers[0]
    #     else:
    #         while num < (len(numbers) - 1):
    #             print("Current ans : ", ans)
    #             ans **= numbers[num + 1]
    #             num += 1
    #
    #     return "Its : " + str(ans)
    # except:
    #     return "Something went wrong."
    # ------ MODERN APPROACH ----------------#
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x ** y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


def div(inp):
    # ------ GENERAL APPROACH ----------------#
    try:
        numbers = re.findall('\d+', inp)
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        ans = numbers[0] / numbers[1]
        return "Its " + str(ans)
    except:
        return "Something went wrong"
    # ------ MODERN APPROACH ----------------#
    # try:
    #     numbers = re.findall('\d+', inp)
    #     numbers = list(map(int, numbers))
    #     sum = reduce(lambda x, y: x / y, numbers)
    #     return "Its " + str(sum)
    # except:
    #     return "Something went wrong."


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


# ----------------------------------------------------- Mapping -------------------------------------------------------#
mapping = {
    "time": tell_time,
    'daily': daily,
    'international': international,
    "exit": by,

    "joke": tell_joke,
    "meme": show_meme,
    'wiki': wiki,
    'temperature': temperature,
    'weather': weather,

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

    "select": select,
    "copy": copy,
    "paste": paste,
    "cut": cut,
    "read": read,

    "add": add,
    "sub": sub,
    "mul": mul,
    "power": power,
    "div": div,

    "track_number": track_number,
    "password": password
}


# -------------------------------------------------------- Chat --------------------------------------------------------#
def chat():
    while True:
        reply = ""
        inp = input("You : ")
        # print("You : ", end=" ")
        # inp = take_command().lower()
        # print(inp)
        for sentence in sent_tokenize(inp):
            # print("you said : ", sentence)                                                     # (You said sentences)
            result = model.predict([bag_of_words(sentence, words)])[0]
            # print(result)                                                                      # (Probability)
            # answer/ user text/ user input etc... Stored in inp
            result_index = numpy.argmax(result)
            tag = labels[result_index]
            # print(tag)  # (Tag)
            bol = False
            ans = ""
            if result[result_index] > 0.7:  # (0.5) works good
                for tg in data['intents']:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                        for key in mapping.keys():
                            if bol == True:
                                break
                            if key == tag:
                                ans = mapping.get(key)(sentence)
                                bol = True
                        if bol == False:
                            ans += random.choice(responses)
            else:
                lst = ['Should i Search More about it?', f"I Think i can show you something about it.",
                       "It sounds Exciting. Let's search it on google ",
                       'I am preety excited.', ' We can Explore more about it',
                       'it sounds amazing I Wanna Explore on Google',
                       'Thanks, To Give me, A Chance but, Lets make a Google search']
                print(random.choice(lst))
                print("Please Confirm")
                ask = input("You : ").lower()
                lst = ['ok', 'sure', 'definitely', 'yup', "yep", "respectable", "of course", "green light", "confirm",
                       "okeydokey", "surely", "satisfactory", "tolerable", "correct", "good", "not bad",
                       "up to scratch",
                       "accurate", "no problem", "alright", "yes", "Here we go", "sounds good", "alright then",
                       "absolutely",
                       "as you say"]
                for word in lst:
                    if word in ask:
                        wiki(sentence)
                        ans += "Here we Go...!"
                else:
                    ans += "okay"
            # print("Grace : ", str(ans))
            reply += str(ans) + ", "
        print("Grace : ", reply)
        speak(reply)


# --------------------------------------------------- Main function ----------------------------------------------------#

if __name__ == '__main__':
    chat()

