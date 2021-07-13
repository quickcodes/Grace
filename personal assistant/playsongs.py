import random
import pywhatkit as pwk
import pyttsx3  # voice setup

#
# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()


# THIS SONG TEACH ME VERY MUCH
# SONG - "i only watch it for the weather by the delegates"

@staticmethod
def daily():
    lst = ['when we were kids', 'wrap me down', 'sunday best',
           'break my stride', 'deep end', 'women like you',
           'holy', 'devil eyes', 'everything at once',
           'runaway', 'i need a dollar', 'willow', 'mask off',
           'back at it', 'peachese', 'into your arms',
           'counting stars', "i only watch it for the weather by the delegates"]
    word = lst[random.randint(0, len(lst) - 1)]
    try:
        pwk.playonyt(word)
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Enjoy {word} from your {compliment} daily mixers")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def mood():
    lst = ['levitating feat dababy', 'post malone feat rani', 'yummy justin biber',
           'astronaut in the ocean', 'love me like you do', 'women like you',
           'sunflower post malone', 'devil eyes', 'let me love you',
           'runaway', 'i need a dollar', 'dance monkey', 'stuck with you',
           'intention', 'never really knew', 'only be me', 'ghost confetti',
           'peace of your heart', '911 r3hab', 'blinding lights', 'not afraid',
           'daisy ashnikko', 'love your voice']
    word = lst[random.randint(0, len(lst) - 1)]
    try:
        pwk.playonyt(word)
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Enjoy {word} from your {compliment} Moody songs")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def mix():
    try:
        pwk.playonyt("Top songs")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Enjoy best music from your {compliment} Moody artist")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def lofi():
    try:
        pwk.playonyt("Lofi songs")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Enjoy {compliment} Lofi music")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def romantic():
    try:
        pwk.playonyt("romantic songs")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Wow Mood is going Romantic. Preety Exciting.\n Here is {compliment} romantic song from you")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def international():
    try:
        pwk.playonyt("top international")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Here is {compliment} song for you")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def party():
    try:
        pwk.playonyt("party songs")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Party.. Yay I am very excited. I Love Party songs.\n Here is {compliment} music from you")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def hindi():
    try:
        pwk.playonyt("top hindi")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"We indians Love songs Here is {compliment} music from you")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def bhojpuri():
    try:
        pwk.playonyt("bhojpuri songs")
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"I am preety excited. Its time to Listen {compliment}, Bhojpuri songs. Yay!")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def sad():
    try:
        pwk.playonyt("sad songs")
        speak(f"I can't Listen that type of songs. Emjoy alone. SEE YAA")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def calm():
    try:
        lst = ['crazy in love by sofia karlberg', 'salted wound by sia']
        word = lst[random.randint(0, len(lst) - 1)]
        pwk.playonyt(word)
        txt = ['favourate', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Enjoy {word} of {compliment} artist")
    except:
        speak("Something wrong happening. Please Try again")


@staticmethod
def song():
    lst = ['levitating feat dababy', 'post malone feat rani', 'yummy justin biber',
           'astronaut in the ocean', 'love me like you do', 'women like you',
           'sunflower post malone', 'devil eyes', 'let me love you',
           'runaway', 'i need a dollar', 'dance monkey', 'stuck with you',
           'intention', 'never really knew', 'only be me by droeloe', 'ghost confetti',
           'peace of your heart', '911 r3hab', 'blinding lights', 'not afraid',
           'daisy ashnikko', 'love your voice', 'crazy in love by sofia karlberg',
           'salted wound by sia', 'counting stars', 'falling trevor daniel'
                                                    'when we were kids', 'wrap me down', 'sunday best',
           'no idea don toliver'
           'break my stride', 'deep end', 'death bad', 'mood feat iann dior',
           'holy', 'everything at once', 'willow', 'mask off', 'love the way you lie',
           'back at it', 'peachese', 'into your arms', 'therefore i am billee eilish',
           "i only watch it for the weather by the delegates"
           ]
    word = lst[random.randint(0, len(lst) - 1)]
    try:
        pwk.playonyt(word)
        txt = ['favourite', 'top', 'great', 'amazing', 'exciting', 'Awesome', 'best']
        compliment = txt[random.randint(0, len(txt) - 1)]
        speak(f"Enjoy {word} of {compliment} artist")
    except:
        speak("Something wrong happening. Please Try again")


PlaySongs = type("PlaySongs", (), {
    "daily": daily,
    "mood": mood,
    "mix": mix,
    "lofi": lofi,
    "romantic": romantic,
    "international": international,
    "party": party,
    "hindi": hindi,
    "bhojpuri": bhojpuri,
    "sad": sad,
    "calm": calm,
    "song": song
})
