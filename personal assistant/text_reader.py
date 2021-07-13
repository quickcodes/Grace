import pyttsx3
import os
from tkinter import filedialog

# voice setup
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id)


# speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# format text
def comaMaker(str):
    count = 0
    new_str = ""
    # adding double spaces
    for word in str:
        if word == " ":
            word += " "
        new_str += word

    # main work
    nxt_str = ""
    for word in new_str:
        if count == 5:  # words
            word += word.replace(" ", ". ")
            count = 0
        if word == " ":
            count += 1
        nxt_str += word
    nxt_str = nxt_str.replace("  ", " ")
    nxt_str = nxt_str.replace(" .", ".")
    return nxt_str


# ----------------------------------------------------------------------------------------------------------------------

os.system("color f0")

fd = filedialog.askopenfilename()

# print("Please. Enter the name of file ")
# speak("Please. Enter the name of file ")
# fin = input("--> ")
fout_txt = ""

str_txt = ""
try:
    with open(fd, encoding="utf8") as f:
        for line in f:
            str_txt += line
    str_txt = str_txt.replace('\n', ' ')
    single_spaces = ' '.join(str_txt.split())
    single_spaces = single_spaces.replace('.', '.\n')
    single_spaces = comaMaker(single_spaces)
    fout_txt += single_spaces

except SyntaxError:
    print("Something went wrong..")
    speak("Something went wrong..")

# ---------------------------------------------------------------------------------------------------------------------
# speaking the book
print("For better Experience. I format your doc According to my taste.")
speak("For better Experience. I format your doc According to my taste.")
os.system("cls")
try:
    print("Lets start listening...")
    speak("Lets start listening...")
    newlst = fout_txt.split('.')

    for word in newlst:
        print(word)
        speak(word)
    print("..\n\nBook or File is completed...\n Hopefully you enjoyed it. Bye Bye")
    speak("..\n\nBook or File is completed...\n Hopefully you enjoyed it. Bye Bye")
except:
    print("Something went wrong..")
    print("Sometime the text format inside text file is different.")
