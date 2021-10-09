import pyttsx3  # voice setup
import datetime  # date and time
import requests
import speech_recognition as sr  # speech recognization
import wikipedia
import webbrowser
import os  # operating system
import turtle  # Creative/Drawing purpose
import time
import subprocess  # OS
import random
from star import star
import daytime  # file to tell time date day
import playsongs  # file to play songs
import stone_paper_scissors  # file to play stone paper scissors
import pywhatkit as pwk
import weather
import pyautogui
import keyboard
import PyDictionary as pd
from playsound import playsound
import sys


# BASIC AND IMPORTANT SETUP --------------------------------------------------------------------------------------------
# VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[5].id)  # total 14(0-13) voices are available


# GRACE REPLIES
class Reply:
    @staticmethod
    def hey():
        lst = [f"Hey , What's Up", "Hello, My friend", f"What is Up ",
               f"It's a Pleasure, To Meet you ", "Hey, Good to See you", "Hey, Great to See you",
               f"Hello {user.name} How are you?", "Hi There", "What's Going On", "What's Happening",
               "How Are You Doing Today?", "How Are You Feeling Today?", "How Are Things With You?",
               f"Look Who It Is! Let me Check. Oh It's {user.name}, Hello {user.name}", "It's Good to Talk with you",
               "Nice To See You", "Oh No, Look Who It Is!"]
        line = lst[random.randint(0, len(lst) - 1)]
        return line

    @staticmethod
    def pleasure():
        lst = ["I'm happy to Help you", "Thank you for the Opportunity", "It's my Pleasure", "You got it",
               "I’m always happy to help", "Not a problem", "Think, Nothing for it", "That's Okay",
               "The Pleasure was all mine", "Its my pleasure you like it.",
               "Enjoy", "It was no Big deal, Really", "Oh! That's Alright", "Don't mention it"]
        line = lst[random.randint(0, len(lst) - 1)]
        return line

    @staticmethod
    def thank():
        lst = ["Thank you.", "Thanks!", "Thanks so much.", "Thanks a million.", "That’s very kind of you.",
               "You made my day.", "You made my day.", "You made my day.", "I couldn’t have done it without you.",
               "I really want to thank you for your help.", "I really appreciate everything you’ve done.",
               "This means a lot to me.", "Thanks for having my back.", "Thank you for your guidance.",
               "It’s my pleasure.", "I'm really impressed with you"]
        line = lst[random.randint(0, len(lst) - 1)]
        return line

    @staticmethod
    def okay():
        lst = ["Yep", "Respectable", "Of course", "Green light", "Confirm", "Okeydokey", "Surely", "Satisfactory",
               "Tolerable", "Correct", "Good", "Not bad", "Up to scratch", "Accurate", "No problem", "Alright", "Yes",
               "Here We Go", "Sounds Good", "Alright Then", "Absolutely", "As You Say"]
        line = lst[random.randint(0, len(lst) - 1)]
        return line

    @staticmethod
    def okay_general():
        lst = ["Yep", "Respectable", "Of course", "Green light", "Confirm", "Okeydokey", "Surely", "Satisfactory",
               "Tolerable", "Correct", "Up to scratch", "Alright", "Yes",
               "Here We Go", "Sounds Good", "Alright Then", "Absolutely", "As You Say"]
        line = lst[random.randint(0, len(lst) - 1)]
        return line

    @staticmethod
    def going_on():
        lst = ["Fantastic and, Much better now that you are with me.",
               "I am blessed!, And Going great. Hope this status go persists for rest of the day",
               "Literally Amazing, And Well enough to talk with you if you wish to.",
               "Better than some, not as good as others.",
               "Imagining myself having a fabulous vacation",
               "The best I can be. Assuming you’re at your best too.",
               "According to my lawyer I don’t have to answer that question, HAHA, Just kidding, I'm Fine,"
               " Thanks for Asking me",
               "Fantastic! but Wait. Are You Flirting With Me?"]
        line = lst[random.randint(0, len(lst) - 1)]
        return line

    # @staticmethod
    # def laugh():
    #     lst = [" haaahhhhhh haaaa! It's preety funny. Right?",
    #            "ahaaaaahaaaahaaaa, Its funny", "ahahahha, Lol I can't stop laughing"]
    #     line = lst[random.randint(0, len(lst) - 1)]
    #     return line


# SPEAK
def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()


# VOICE RECOGNITION
def take_command():
    # it will take input from microphone
    # and return string as a output
    r = sr.Recognizer()  # take input and store in variable
    with sr.Microphone() as source:
        print("\tListening...")
        speak("listening")
        r.pause_threshold = 0.5
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("\tRecognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"\tYou said: {query}\n\t")
        speak(Reply.okay_general())
    except Exception:
        print("\tPlease say that again...")
        return "\tNone"
    return query


count = 0


# CHECK DATA
def exist(lines):
    global count
    count += 1
    for line in lines:
        if line in query:
            return True


# DEFINING CLASSES -----------------------------------------------------------------------------------------------------
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
        speak(f"Got it Your name is {self.name}")
        print(f"Got it Your name is {self.name}")

    def set_location(self, location):
        self.location = location
        speak(f"All Set... you lived in {self.location} right ? That's great.")


class Assistant:  # ASSISTANT CLASS
    name = "Grace"
    developer = "Dhruv Soni"

    def __init__(self, name="Grace"):
        self.name = name

    def set_name(self, name):
        self.name = name

    def introduce(self):
        speak(f"I am {self.name}")

    @staticmethod
    def wish_me():
        os.system("color f0")
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            lines = ['Good Morning ', 'Great Morning ', 'Happy Morning ', 'Very Very Good Morning ']
            line = lines[random.randint(0, len(lines) - 1)]
            line += User.name
            speak(line)
        elif 12 <= hour < 18:
            lines = ['Good Afternoon ', 'Great Afternoon ', 'Happy Afternoon ', 'Very Very Good Afternoon ']
            line = lines[random.randint(0, len(lines) - 1)]
            line += User.name
            speak(line)
        else:
            lines = ['Good Evening ', 'Great Evening ', 'Happy Evening ', 'Very Very Good Evening ']
            line = lines[random.randint(0, len(lines) - 1)]
            line += User.name
            speak(line)


# OTHER FUNCTIONS ------------------------------------------------------------------------------------------------------


def wiki(query):
    query = query.replace('something', '')
    query = query.replace('about', '')
    query = query.replace('tell me', '')
    query = query.replace('who is', '')
    query = query.replace('do you know', '')
    query = query.replace('know', '')
    query = query.replace('tell', '')
    try:
        result = wikipedia.summary(query, sentences=2)
        txt = ['sure', 'yes', 'yup', 'Its exciting', 'definitely']
        word = txt[random.randint(0, len(txt) - 1)]
        speak(f'{word} {result}')
    except:
        speak(f"Brother Gooogle knows {query}")
        pwk.search(query)
        speak(f"Here is google result's")


def tell_joke():
    json_data = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    first_line = json_data['setup']
    punch_line = json_data['punchline']
    print(first_line)
    speak(first_line)
    time.sleep(2)
    print(punch_line)
    speak(punch_line)


def tell_news():
    number = random.randint(0, 30)
    json_data = requests.get("https://saurav.tech/NewsAPI/top-headlines/category/health/in.json").json()
    title = json_data['articles'][number]['title']
    content = json_data['articles'][number]['content']
    speak("Here is the Title of News")
    print(title)
    speak(title)
    speak("And Here is the Content of News")
    print(content)
    speak(content)


def show_meme():
    json_data = requests.get("https://meme-api.herokuapp.com/gimme").json()
    meme_url = json_data["url"]
    webbrowser.open(meme_url)


def by():
    print("\tBye Bye")
    speak("Bye Bye")
    time.sleep(1)
    exit()


def youtube_auto():
    speak("Should i Play it on Full Screen mode? Say Yes or sure to Confirm")
    ans = take_command().lower()
    if ('yes' in ans) or ('sure' in ans):
        keyboard.press('f')
    return


# TIME TRACKER ---------------------------------------------------------------------------------------------------------
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("________________________________")
        print("\tSearches : ", count)
        print("\tSize of respond : ", sys.getsizeof(respond))
        print("\tSize of exist : ", sys.getsizeof(exist))
        print("\tTime : ", total)
        print("________________________________")
        return rv
    return wrapper


bool_weather = True
bool_wiki = True
bool_hello = True
bool_good = True
bool_songs = True
bool_open = True
bool_close = True
bool_sps = True
bool_time, bool_alarm = True, True
bool_intro, bool_name, bool_cant, bool_friends, bool_featuers = True, True, True, True, True
bool_meaning, bool_syn = True, True
bool_math, bool_shot, bool_read_write = True, True, True


# WORKING WITH RAW DATA ------------------------------------------------------------------------------------------------
@timer
def respond(query):

    global bool_weather, bool_wiki, bool_good, bool_hello, bool_songs, bool_open, bool_close, bool_sps
    global bool_time, bool_intro, bool_name, bool_cant, bool_friends, bool_alarm, bool_meaning, bool_syn
    global bool_math, bool_shot, bool_read_write, bool_featuers
    try:
        print("Start respond")
        print("Query : ", query)
        # HELLO
        if bool_hello and exist(['hello', 'Hi', 'Hola', 'what is up', 'hey', "whatzupp"]):
            txt = ['hello', 'Hi', 'Hola', 'hey']
            word = txt[random.randint(0, len(txt) - 1)]
            speak(f"{word}")
            speak(Reply.hey())
            bool_hello = False
        if bool_name and (('grace' in query) or ("Grace" in query) or ("grass" in query) or ("guess" in query)
                          or ("dress" in query) or ("race" in query)):
            speak("Yes Boss")
            bool_hello = False
            bool_name = False
        # FEATURES
        if bool_featuers and exist(['your features', 'what you can do']):
            bool_featuers = False
            speak(Reply.okay())
            speak('''
            I can tell Time, day, date.
            I can provide you weather details.
            I can draw star.
            And many other thing's are under developement.
            ''')
        if bool_intro and (('are you there' in query) or ('can you hear me' in query)):
            speak("Yes. I am Always here for you")
            bool_intro = False
        if bool_cant and (("you can't" in query) or ("you can not" in query)):
            speak("Every Time, When you say Something to me I try my Best...")
        if bool_intro and (("what about you" in query) or ("what about you" in query) or ("how are you" in query) or
                ("what's going on" in query) or ("what's up" in query) or ("what is up" in query) or (
                "what are you doing" in query)):
            speak(Reply.going_on())
            bool_intro = False
        # FRIENDS
        if bool_friends and exist(['you have any friend', 'about your friend', 'friends you have',
                    'tell me about your friend']):
            lin = ["Some of my all time friends and inspirations are Siri, Alexa, Google assistant",
                   "Anyone who needs help with anything is my friend. Any Everyone needs help with something"]
            comp = lin[random.randint(0, len(lin) - 1)]
            speak(comp)
            bool_friends = False
        # ALARM
        if bool_alarm and (bool_time and exist('set') and exist(['alarm'])):
            speak("Please type time")
            tm = input("Enter Time |H:M:S| :")
            speak("Your Alarm is setted")
            while True:
                raw_tm = datetime.datetime.now()
                now = raw_tm.strftime("%H:%M,%S")
                if tm == now:
                    speak("It's Time to wakup")
                    playsound("Alessia_Cara.mp3")
                    time.sleep(20)
                    bool_alarm = False
                    break
        # PLAY SONGS ---------------------------------------------------------------------------------------------------
        if bool_songs and exist(['sing a song', 'i want to dance with you']):
            lst = ['Okay', 'ofcourse', 'Sure', 'It sounds exciting', 'I am preety excited',
                   'I think its amazing', 'Thank to give me a chance ']
            word = lst[random.randint(0, len(lst) - 1)]
            speak(f"{word}. Here is a best song from me")
            playsongs.PlaySongs.song()
        elif bool_songs and exist(['play', 'song', 'songs', 'music', 'musics']):
            bool = False
            if ('full' in query) and ('screen' in query):
                bool = True
                query.replace('full','')
                query.replace('screen','')
            # WITH ME
            if exist(['with me']):
                lst = ['moody', 'romantic', 'dramatic', 'exciting', 'daily', 'amazing', 'or..... sexy']
                word = lst[random.randint(0, len(lst) - 1)]
                speak(f"Did i play something {word}")
            # DAILY
            elif exist(['something easy', 'daily', 'daily', 'daily songs', 'daily song', 'daily song',
                        'delhi', 'delhi', 'delhi songs', 'delhi song', 'delhi song']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing your Daily songs")
                playsongs.PlaySongs.daily()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()

            # MOOD
            elif exist(['something moody', 'mood', 'moody', 'moody songs', 'moody song', 'mood song',
                        'something 2d', '2d', '2d', '2d songs', '2d song', '2d song']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing Best Moody songs")
                playsongs.PlaySongs.mood()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # MIX
            elif exist(['something mix', 'mix', 'mixy', 'mix songs', 'mixy song', 'mix song',
                        'something fix', 'mfx', 'fixy', 'fix songs', 'fixy song', 'fix song',
                        'something vix', 'vix', 'vixy', 'vix songs', 'vixy song', 'vix song']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing Best Mix songs")
                playsongs.PlaySongs.mix()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # ROMANTIC
            elif exist(['romantic', 'romanchak']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing Best romantic songs")
                playsongs.PlaySongs.romantic()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # PARTY
            elif exist(['party', 'for dance']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing Best Party songs")
                playsongs.PlaySongs.party()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # BHOJPURI
            elif exist(['bhojpuri', 'bhojpuri', 'bhojpuri']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing Bhojpuri songs")
                playsongs.PlaySongs.bhojpuri()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # SAD
            elif exist(['sad', 'down', 'bad', 'upset']):
                txt = ['okay', 'sure', 'its not good', 'ohh', 'why']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} As your wish I am playing sad songs")
                playsongs.PlaySongs.sad()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # SEXY
            elif exist(['something sexy', 'sexy songs', 'sexy song', 'sexy',
                        'something sexi', 'sexi songs', 'sexi song', 'sexi',
                        'something sex', 'sex songs', 'sex song', 'sex']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I then now its my responsitility to maintaine your mood")
                playsongs.PlaySongs.sexy()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # LOFI
            elif exist(['lofi', 'Lofi', 'chill', 'relaxing', 'midnight', 'study', 'Loafer']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I also like this type of songs lets enjoy it together")
                playsongs.PlaySongs.lofi()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # INTERNATIONAL
            elif exist(['international', 'top', 'recommended', 'english']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} Here is best songs for you")
                playsongs.PlaySongs.international()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # HINDI
            elif exist(['hindi', 'indian', 'hindustani', 'bharat']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} Here is best Hindi songs for you")
                playsongs.PlaySongs.hindi()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # SONGS
            elif exist(['some songs', 'songs', 'song', 'something on youtube', 'something nice']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                speak(f"{word} {user.name} I am Playing Best songs")
                playsongs.PlaySongs.song()
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            # YOUTUBE
            elif exist(['on youtube', 'on YouTube']):
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                query = query.replace("on", "")
                query = query.replace("youtube", "")
                query = query.replace("something", "")
                query = query.replace("in", "")
                query = query.replace("play", "")
                speak(f"{word} {user.name} I am Playing {query} on YouTube")
                pwk.playonyt(query)
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
            else:
                txt = ['okay', 'sure', 'yes', 'yup', 'Yay', 'wow', 'exciting', 'hurrah']
                word = txt[random.randint(0, len(txt) - 1)]
                query = query.replace("on", "")
                query = query.replace("youtube", "")
                query = query.replace("something", "")
                query = query.replace("in", "")
                query = query.replace("play", "")
                speak(f"{word}. {user.name}. I am Playing {query} on YouTube")
                # webbrowser.open('https://www.youtube.com/results?search_query=' + query)
                pwk.playonyt(query)
                time.sleep(6)
                if bool: keyboard.press("f")
                else:youtube_auto()
        elif bool_sps and exist(['stone', 'paper', 'scissors']):
            stone_paper_scissors.stone_paper_scissor()
        # TELL ME ------------------------------------------------------------------------------------------------------
        # MEANING
        if bool_meaning and exist(['meaning', 'example']):
            word = query.split("of")[1]
            res = pd.PyDictionary.synonym(word)
            speak(f"Meaning of {word} is {res}")
            bool_meaning = False
        # SYNONYM
        if bool_syn and exist(['synonym']):
            word = query.split("of")[1]
            res = pd.PyDictionary.synonym(word)
            speak(f"Meaning of {word} is {res}")
            bool_syn = False
        # DAY, MONTH, YEAR
        elif exist(['current', 'right now', 'tell me', 'what is']) and exist(['day', 'date', 'year', 'week', 'month']):
            daytime.DayTime.tell_dmy()
            bool_time = False
        # TIME
        elif exist(['current', 'right now', 'tell me', 'what is']) and ("time" in query):
            daytime.DayTime.tell_time()
            bool_time = False
        # JOKE
        elif ("joke" in query) and ("tell"):
            print("inside joke")
            speak(Reply.okay())
            tell_joke()
            tell_joke()
            # speak(Reply.laugh())
        # NEWS
        elif ("news" in query) and ("tell"):
            speak(Reply.okay())
            tell_news()
        # PRICE OF
        elif exist(['price of']) and exist(['tell', 'what', 'show']):
            speak(Reply.okay())
            search_for = query.split('of')[-1]
            url = "https://google.com/search?q=" + search_for
            webbrowser.open(url)
        # MEME
        elif ("meme" in query) and ("tell" or "show"):
            speak(Reply.okay())
            show_meme()
            # speak(Reply.laugh())
            speak("Here is a Meme. Enjoy it")
        # ABOUT ME
        elif exist(['your boss', 'your owner', 'your developer', 'your god', 'your master']):
            speak(f"You, are the only one In this entire world who can talk with. MISS {assi.name}")
        elif exist(['tell me about me', 'tell me about myself', 'do you know me', 'who am i']):
            speak(Reply.okay())
            speak(f'I know that your name is {user.name}. And you are living in {user.location}'
                  f'And Ya. You are wonderful in coding. Plus you ask me great questions. I couldnt ask '
                  f'for better boss')
        # ABOUT YOURSELF
        elif ('what is your name' in query) or ('you have any name' in query):
            speak(f"My name {assi.name}")
        elif exist(['tell me about you', 'tell me about yourself', 'do you know you', 'who are you']):
            lin2 = ['I can play music for you', 'I can provide you weather detail',
                    'I can write notes for you', 'I can try to sing a song for you',
                    ]
            work = lin2[random.randint(0, len(lin2) - 1)]
            speak(Reply.okay())
            speak(f'I am your {assi.name}. {work}'
                  f'And I am here to make your Things easier than ever. Just tell me')
        # TELL ABOUT.....
        elif exist(['tell me about', 'tell me something about', 'do you know', 'who is', 'do you know']):
            if exist(['alexa', 'siri', 'google', 'Google']):
                lst = ['Please dont say any one but. SHE is my CRUSH', 'My crush, My inspiration',
                       "My love. Oh no i mean my loyal friend",
                       'She is preety amazing i like the way she move i mean work',
                       ]
                word = lst[random.randint(0, len(lst) - 1)]
                speak(word)
            elif exist(['my friends', 'my friend']):
                speak("I know one of your friend. Her name is Elva. Oh wow Its me.")
            elif exist(['weather', 'mosam', 'outside', 'city']):
                weather.weather("indore")
                bool_weather = False
            else:
                bool_wiki = False
                wiki(query)
        # YOU ARE
        elif exist(['you are', 'your']) and exist(['awesome', 'crazy', 'wonderful', 'amazing', 'insane', 'good', 'nice',
                                                   'kind', 'cool', 'better']):
            speak(Reply.thank())
            bool_good = False
        # ENTERTAIN
        elif exist(['draw', 'entertain me', 'star']):
            speak("Should i draw cool star for you ?")
            ask = take_command().lower()
            lst = ['ok', 'sure', 'definitely', 'yup', "yep", "respectable", "of course", "green light", "confirm",
                   "okeydokey", "surely", "satisfactory", "tolerable", "correct", "good", "not bad", "up to scratch",
                   "accurate", "no problem", "alright", "yes", "Here we go", "sounds good", "alright then", "absolutely",
                   "as you say"]
            for word in lst:
                if word in ask:
                    a = turtle.Turtle()
                    a.getscreen().bgcolor("black")
                    a.penup()
                    a.goto(-200, 100)
                    a.pendown()
                    a.color("yellow")
                    a.speed(25)
                    star(a, 360)
                    turtle.done()
            else:
                speak("Hopefully you liked it")
        # STONE PAPER SCSISSORS
        elif bool_sps and exist(["game"]) and exist(['stone', 'paper', 'scissors']):
            stone_paper_scissors.stone_paper_scissor()
        print("Middle respond")
        print("Query : ", query)
        # OPEN THINGS ------------------------------------------------------------------------------------------------------
        if exist(['open', 'run']):
            if exist(['your mouth', 'you are mouth']):
                speak("Ha Ha Ha")
            elif ('new' in query) and ('tab' in query):
                try:
                    keyboard.press_and_release('ctrl + t')
                    speak(Reply.okay())
                    speak("New and Fresh tab is Opening")
                except:
                    speak("Unable to Open New Tab for You")
            elif bool_sps and exist(['stone', 'paper', 'scissors']):
                stone_paper_scissors.stone_paper_scissor()
            # SUBLIME TEXT EDITOR
            elif exist(['sublime', 'sublime', 'code editor']):
                speak(Reply.okay())
                speak(f"{user.name}. I am opening Sublime text editor")
                try:
                    subprocess.Popen("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
                except:
                    speak(f"I am unable to open Sublime text editor. Please make a contact with {user.name}")
            # VISUAL STUDIO
            elif exist(['vs ', 'vs ', 'visual studio', 'visual studio']):
                speak(Reply.okay())
                speak(f"{user.name}. I am opening Visual Studio")
                try:
                    subprocess.Popen("C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                except:
                    speak(f"I am unable to open Visual studio code. Please make a contact with {user.name}")
                # PYCHARM
            # PYCHARM
            elif exist(['pycharm', 'pycharm', 'python pro']):
                speak(Reply.okay())
                speak(f"{user.name}. I am opening pycharm")
                try:
                    subprocess.Popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe")
                except:
                    speak(f"I am unable to open Pycharm. Please make a contact with {user.name}")
                # NOTEPAD
            # NOTEPAD
            elif exist(['notepad', 'notepad', 'note pad', 'note pad']):
                speak(Reply.okay())
                speak(f"{user.name}. I am opening notepad only for you")
                try:
                    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
                except:
                    speak(f"I am unable to open notepad. Please make a contact with {user.name}")
                # CALCULATOR
            # CALCUALTOR
            elif exist(['calculator', 'calculator']):
                speak(Reply.okay())
                speak(f"{user.name}. I am opening calculator only for you")
                try:
                    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                except:
                    speak(f"I am unable to open Calculator. Please make a contact with {user.name}")
                # WORDPAD
            # WORDPAD
            elif exist(['wordpad', 'wordpad', 'word pad', 'word pad']):
                speak(Reply.okay())
                speak(f"{user.name}. I am opening calculator only for you")
                try:
                    subprocess.Popen('C:\\Windows\\System32\\write.exe')
                except:
                    speak(f"I am unable to open word pad. Please make a contact with {user.name}")
            # BROWSER
            elif exist(['browser', 'microsoft edge', 'edge', ]):
                speak(Reply.okay())
                speak(f"{user.name}. I am Opening Microsoft edge.")
                try:
                    webbrowser.open("https://google.com")
                except:
                    speak(f"I am unable to open Microsoft edge . Please make a contact with {user.name}")
                speak("Here you can browse whatever you want.")
            # WEBSITES -----------------------------------------------------------------------------------------------------
            elif exist(['youtube', 'YouTube']):
                speak(Reply.okay())
                webbrowser.open("https://youtube.com/")
            elif exist(['spotify']):
                speak(Reply.okay())
                webbrowser.open("https://spotify.com/")
            elif exist(['twitter']):
                speak(Reply.okay())
                webbrowser.open("https://twitter.com/")
            elif exist(['instagram']):
                speak(Reply.okay())
                webbrowser.open("https://instagram.com/")
            elif exist(['google', 'Google']):
                speak(Reply.okay())
                webbrowser.open("https://google.com/")
            elif exist(['amazon']):
                speak(Reply.okay())
                webbrowser.open("https://amazon.com/")
            elif exist(['flipkart']):
                speak(Reply.okay())
                webbrowser.open("https://flipkart.com/")
            elif exist(['linkedin']):
                speak(Reply.okay())
                webbrowser.open("https://linkedin.com/")
            else:
                try:
                    speak(Reply.okay())
                    name = query.split('open')[-1]
                    webbrowser.open("https://" + name + ".com/")
                    speak("I am opening" + name)
                except:
                    speak(Reply.okay())
                    name = query.split('open')[-1]
                    webbrowser.open("https://google.com/search?q=" + name)
                    speak("I am opening" + name)
        # CLOST THINGS -----------------------------------------------------------------------------------------------------
        if bool_close and exist(['close', 'kill']):
            speak("Are you sure?")
            speak("say yes to confirm")
            confirm = take_command().lower()
            if ('yes' in confirm) or ('sure' in confirm):
                bool_close = False
                if exist(['your mouth', 'you are mouth']):
                    speak("Na Na Na")
                # SUBLIME TEXT EDITOR
                elif ('tap' in query) or ('tab' in query) or ('time' in query):
                    try:
                        keyboard.press_and_release('ctrl + w')
                        speak(Reply.okay())
                        speak("Your Current tab is closed")
                    except:
                        speak("Unable to Open New Tab for You")
                elif exist(['sublime', 'sublime', 'code editor']):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am Closing Sublime text editor")
                    try:
                        os.system("TASKKILL /F /im sublime_text.exe")
                    except:
                        speak(f"I am unable to Close Sublime text editor. Please make a contact with {user.name}")
                # VISUAL STUDIO
                elif exist(['vs ', 'vs ', 'visual studio', 'visual studio']):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am opening Visual Studio")
                    try:
                        os.system("TASKKILL /F /im Code.exe")
                    except:
                        speak(f"I am unable to Close Visual studio code. Please make a contact with {user.name}")
                    # PYCHARM
                # PYCHARM
                elif exist(['pycharm', 'pycharm', 'python pro']):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am opening pycharm")
                    try:
                        os.system("TASKKILL /F /im pycharm64.exe")
                    except:
                        speak(f"I am unable to Close Pycharm. Please make a contact with {user.name}")
                    # NOTEPAD
                # NOTEPAD
                elif exist(['notepad', 'notepad', 'note pad', 'note pad']):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am opening notepad only for you")
                    try:
                        os.system("TASKKILL /F /im notepad.exe")
                    except:
                        speak(f"I am unable to Close notepad. Please make a contact with {user.name}")
                    # CALCULATOR
                # CALCUALTOR
                elif exist(['calculator', 'calculator']):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am opening calculator only for you")
                    try:
                        os.system("TASKKILL /F /im calc.exe")
                    except:
                        speak(f"I am unable to close Calculator. Please make a contact with {user.name}")
                    # WORDPAD
                # WORDPAD
                elif exist(['wordpad', 'wordpad', 'word pad', 'word pad']):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am opening calculator only for you")
                    try:
                        os.system("TASKKILL /F /im write.exe")
                        subprocess.Popen('C:\\Windows\\System32\\write.exe')
                    except:
                        speak(f"I am unable to Close word pad. Please make a contact with {user.name}")
                # BROWSER
                elif exist(['browser', 'microsoft edge', 'edge', ]):
                    speak(Reply.okay())
                    speak(f"{user.name}. I am Opening Microsoft edge.")
                    try:
                        os.system("TASKKILL /F /im google.exe")
                    except:
                        speak(f"I am unable to open Microsoft edge . Please make a contact with {user.name}")
                    speak("Here you can browse whatever you want.")
                # WEBSITES -----------------------------------------------------------------------------------------------------
                elif exist(['spotify']):
                    speak(Reply.okay())
                    webbrowser.open("https://spotify.com/")
                elif exist(['twitter']):
                    speak(Reply.okay())
                    webbrowser.open("https://twitter.com/")
                elif exist(['instagram']):
                    speak(Reply.okay())
                    webbrowser.open("https://instagram.com/")
                elif exist(['google', 'Google']):
                    speak(Reply.okay())
                    webbrowser.open("https://google.com/")
                elif exist(['amazon']):
                    speak(Reply.okay())
                    webbrowser.open("https://amazon.com/")
                elif exist(['flipkart']):
                    speak(Reply.okay())
                    webbrowser.open("https://flipkart.com/")
                elif exist(['linkedin']):
                    speak(Reply.okay())
                    webbrowser.open("https://linkedin.com/")
                else:
                    try:
                        speak(Reply.okay())
                        name = query.split('open')[-1]
                        webbrowser.open("https://" + name + ".com/")
                        speak("I am opening" + name)
                    except:
                        speak(Reply.okay())
                        name = query.split('open')[-1]
                        webbrowser.open("https://google.com/search?q=" + name)
                        speak("I am opening" + name)
        # TEXT READER
        if bool_read_write and exist(['read text', 'text to speech', 'read for me', 'open text reader', 'text reader']):
            try:
                speak(Reply.okay())
                speak(f"{user.name}. please select text file")
                import text_reader
                speak("Hopefully you liked it")
            except:
                speak(f"Something went wrong {user.name}")
            finally:
                bool_read_write = False
            # NOTE WRITER
        # NOTE MAKER
        elif  bool_read_write and exist(['write it down', 'make a note', 'write note', 'write it', 'right it', 'note it']):
            try:
                note = ""
                lst = ['done', 'save it', 'save']
                lst1 = ['delete', 'remove', 'discard it']
                speak(Reply.okay())
                speak(f"{user.name}. please say Clear and loud because i am writing")
                while True:
                    speak("I am writing now")
                    raw = take_command()
                    for word in lst:
                        if word in raw:
                            speak("I am saving your note ")
                            file = open('note.txt', 'w')
                            file.write(note)
                            file.close()
                            exit()
                    for word in lst1:
                        if word in raw:
                            speak(f"Done {user.name}. By By")
                            exit()
                    note += " " + raw
            finally:
                bool_read_write = False
        # BASIC STUFF ------------------------------------------------------------------------------------------------------
        # SCREENSHOT
        if bool_shot and exist(['take', 'capture']) and exist(['screenshot', 'snapshot', 'screen']):
            try:
                speak("What should i name that?")
                name = take_command().lower()
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save("E:\\" + name + ".png")
                speak("Your ScreenShot is saved in E Drive as a png format")
            except:
                speak("I think, The location to save ScreenShot is not Correct")
                speak("This feature is comming soon")
            finally:
                bool_shot = False
        # EXCITING
        if bool_good and exist(['awesome', 'wonderful', 'amazing', 'exciting', 'wow', 'cool', 'nice', 'good', 'kind', 'crazy']):
            speak("Yaah, It is " + query)
            bool_good = False
        # BLESSED
        elif exist(['thanks', 'thank you']):
            speak(Reply.pleasure())
        # NO
        elif exist(['no', 'nope']):
            speak("okay")
        # BYE
        elif exist(['by', 'bye', 'then by', 'okay by']):
            by()
        # OKAY, GOT IT ETC....................
        elif bool_good and exist(['ok', 'sure', 'definitely', 'yup', "yep", "respectable", "of course", "green light", "confirm",
                    "okeydokey", "surely", "satisfactory", "tolerable", "correct", "good", "not bad", "up to scratch",
                    "accurate", "no problem", "alright", "yes", "Here we go", "sounds good", "alright then", "absolutely",
                    "as you say"]):
            speak(Reply.okay())
            bool_good = False
        if exist(['I am', "I'm"]):
            if exist(["excited", "amazing", "awesome", "great", "creative", "nice", "good", "best", "happy", "insane",
                      "hero", "wonderful"]):
                speak("Your are Looking happy Today. Do You wanna Share Something with me")
        elif exist(['know', 'am awesome', 'am amazing', 'am great']):
            lst = [f'Yes you are awesome {user.name}', 'We are amazing', 'No one can beat us', 'You are Unstoppable']
            word = lst[random.randint(0, len(lst) - 1)]
            speak(word)
        # WEATHER
        if exist(['weather', 'mosam', 'outside', 'about city', 'weather details']):
            weather.weather("indore")
            bool_weather = False
        # MATHS
        if exist(['+', '-', '*', 'x', '/', 'power', 'plus', 'minus', 'into', 'multiply', 'divide', 'calculate']):
            speak(Reply.okay())
            # query.replace('calculate', '')
            if 'calculate' in query:
                word = "calculate"
                wordlist = query.split()
                query = [x for x in wordlist if x not in word]
                print("query: ", query)
                try:
                    if exist(['+', 'plus']):
                        speak("Its")
                        speak(int(query[0]) + int(query[2]))
                    elif exist(['-', 'minus']):
                        speak("Its")
                        speak(int(query[0]) - int(query[2]))
                    elif exist(['*', 'x', 'into', 'multiply']):
                        speak("Its")
                        speak(int(query[0]) * int(query[2]))
                        print("query: ", query)
                    elif exist(['/', 'divide']):
                        speak("Its")
                        try:
                            speak(int(query[0]) - int(query[2]))
                        except:
                            speak(query)
                    elif exist(['**', 'power']):
                        speak("Its")
                        speak(int(query[0]) ** int(query[2]))
                except:
                    speak("Can you Please say numbers more clear ?")
            else:
                try:
                    if exist(['+', 'plus']):
                        speak("Its")
                        speak(int(query.split()[0]) + int(query.split()[2]))
                    elif exist(['-', 'minus']):
                        speak("Its")
                        speak(int(query.split()[0]) - int(query.split()[2]))
                    elif exist(['*', 'x', 'into', 'multiply']):
                        speak("Its")
                        speak(int(query.split()[0]) * int(query.split()[2]))
                        print("query: " + query)
                    elif exist(['/', 'divide']):
                        speak("Its")
                        try:
                            speak(int(query.split()[0]) - int(query.split()[2]))
                        except:
                            speak(query)
                    elif exist(['**', 'power']):
                        speak("Its")
                        speak(int(query.split()[0]) ** int(query.split()[2]))
                except:
                    speak("Can you Please say numbers more clear ?")
        # OTHER ------------------------------------------------------------------------------------------------------------
        # CHANGE NAME
        if exist(['my name is']):
            user.set_name(query)
            speak(Reply.okay())
            speak(f"So, Your name is, {user.name}")
        # BLUETOOTH, CAMERA, WIFI, LIGHTS
        elif exist(['can you', 'turn on', 'turn off']):
            if exist(['bluetooth', 'Bluetooth', 'wifi', 'camera', 'lights', 'lights']):
                lst = ['It sounds exciting', 'I am preety excited',
                       'I think its amazing', 'Thank to give me a chance ']
                word = lst[random.randint(0, len(lst) - 1)]
                speak(Reply.okay())
                speak(f"{word}. But It's my bad luck i can't do that for you")
                speak("But I can search any thing for you")
            else:
                speak("I am becoming Everyday better and better. Hopefully I future i will do that for you")

        elif (bool_weather and  bool_wiki and  bool_good and  bool_hello and  bool_songs and  bool_open) and \
            (bool_close and  bool_sps and bool_time and  bool_intro and  bool_name and  bool_cant and bool_friends) and \
            (bool_alarm and  bool_meaning and  bool_syn and bool_math and  bool_shot and  bool_read_write) and \
            (bool_featuers):
            lst = ['Should i Search More about it?', f"I Think i can show you something about it.",
                   "It sounds Exciting. Let's search it on google ",
                   'I am preety excited.', ' We can Explore more about it',
                   'it sounds amazing I Wanna Explore on Google',
                   'Thanks, To Give me, A Chance but, Lets make a Google search']
            word = lst[random.randint(0, len(lst) - 1)]
            speak(word)
            speak("Please say Yes or Sure to Confirm")
            ask = take_command()
            lst = ['ok', 'sure', 'definitely', 'yup', "yep", "respectable", "of course", "green light", "confirm",
                   "okeydokey", "surely", "satisfactory", "tolerable", "correct", "good", "not bad", "up to scratch",
                   "accurate", "no problem", "alright", "yes", "Here we go", "sounds good", "alright then",
                   "absolutely",
                   "as you say"]
            for word in lst:
                if word in ask:
                    pwk.search(query)
        print("End respond")
        print("Query : ", query)
        print(bool_weather, bool_wiki, bool_good, bool_hello, bool_songs, bool_open, bool_close, bool_sps,
            bool_time, bool_intro, bool_name, bool_cant, bool_friends, bool_alarm, bool_meaning, bool_syn,
            bool_math, bool_shot, bool_read_write, bool_featuers)
    except:
        print("Hello world")




# MAIN -----------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        query = ""
        assi = Assistant()
        assi.wish_me()
        # assi.introduce()
        user = User()
        speak(Reply.hey())
        while True:
            query = take_command().lower()
            respond(query)
            count = 0
    except Exception as e:
        print(e)





