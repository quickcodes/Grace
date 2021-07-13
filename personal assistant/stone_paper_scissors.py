import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    ''' It takes input from microphone
    and give string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query

def gameWin(comp, query):
    try:
        global you
        if "stone" in query:
            you = "stone"
            if comp=="paper" or comp == "scissors":
                speak("you win")
            else:
                speak("Our match is draw")
        elif "paper" in query:
            you = "paper"
            if comp=="stone" or comp=="scissor":
                speak("you win")
            else:
                speak("Our match is draw")
        elif "scissor" in query:
            you = "scissor"
            if comp=="stone" or comp=="paper":
                speak("You win")
            else:
                speak("Our match is draw")
        else:
            speak("Different minded")


    except:
        raise SyntaxError("Please enter valid input. ")


def stone_paper_scissor():
    speak("Lets play a stone paper scissors game")
    while True:
        comp = ""
        randNo = random.randint(1, 3)
        if randNo == 1:
            comp = 'stone'
        elif randNo == 2:
            comp = 'paper'
        elif randNo == 3:
            comp = 'scissors'

        speak(" I already choose my option ")
        speak(" Its your turn choose from: Stone, Paper or scissors . Or if you want exit say Exit or Quit")
        query = takeCommand().lower()
        if "exit" in query :
            speak("Nice to meet You! By By")
            exit()
        elif "quit" in query:
            speak("Nice to meet You! By By")
            exit()
        gameWin(comp, query)

        speak(f"I choosed {comp}")
        speak("Its all about fun...! Lets Play again....")













