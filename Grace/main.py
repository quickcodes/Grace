import random
import json
import torch
import wikipedia, pywhatkit as pwk
from model import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

# -----------------------------------------------------------------------------------------------------------
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)
FILE = "TrainData.pth"
data = torch.load(FILE)
# ------------------------------------------------------------------------------------------------------------
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
# ------------------------------------------------------------------------------------------------------------
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()
# ------------------------------------------------------------------------------------------------------------
Name = "Grace"
# ------------------------------------------------------------------------------------------------------------
from listen import take_command
from Speaker import speak
from features import calc, other, play, password_crack, close_software, open_software
# ------------------------------------------------------------------------------------------------------------
import requests, webbrowser


# --------------------------------------------------- Api Functions ----------------------------------------------------#


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
    var = play.PlaySongs.daily()
    print("Played")
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def international(inp):
    var = play.PlaySongs.international()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def mood(inp):
    var = play.PlaySongs.mood()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def mix(inp):
    var = play.PlaySongs.mix()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def lofi(inp):
    var = play.PlaySongs.lofi()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def romantic(inp):
    var = play.PlaySongs.romantic()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def party(inp):
    var = play.PlaySongs.party()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def hindi(inp):
    var = play.PlaySongs.hindi()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def bhojpuri(inp):
    var = play.PlaySongs.bhojpuri()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def sad(inp):
    var = play.PlaySongs.sad()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def calm(inp):
    var = play.PlaySongs.calm()
    play.youtube_auto(inp)  # for full screen mode
    return "Here we go!..."


def song(inp):
    var = play.PlaySongs.song()
    play.youtube_auto(inp)  # for full screen mode
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
    print("sublime")
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


def by(inp):
    print("bye bye")
    print("You can call me any time by saying my Name like, Hello Grace")
    time.sleep(2)
    exit()


# ----------------------------------------------------- Mapping -------------------------------------------------------#
mapping = {
    # tag: function
    "time": tell_time,
    'daily': play.PlaySongs.daily,
    'international': play.PlaySongs.international,
    "mood": play.PlaySongs.mood,
    "mix": play.PlaySongs.mix,
    "lofi": play.PlaySongs.lofi,
    "romantic": play.PlaySongs.romantic,
    "party": play.PlaySongs.party,
    "hindi": play.PlaySongs.hindi,
    "bhojpuri": play.PlaySongs.bhojpuri,
    "sad": play.PlaySongs.sad,
    "calm": play.PlaySongs.calm,
    "song": play.PlaySongs.song,

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

    "add": calc.add,
    "sub": calc.sub,
    "mul": calc.mul,
    "power": calc.power,
    "div": calc.div,

    "track_number": other.track_number,
    "password": password_crack.main
}

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


def get_clean_data(data: str) -> str:
    text = data.lower()
    tokens = tokenizer.tokenize(text)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(tokens) for tokens in new_tokens]
    clean_text = " ".join(stemmed_tokens)
    return clean_text


from nltk.tokenize import sent_tokenize
import time


def chat():
    reply = ""
    # inp = input("You : ")
    # print("You : ", end=" ")
    inp = take_command().lower()
    print(inp)
    if inp == "quit":
        exit()
    # -------------------------------------------------------------------
    for sentence in sent_tokenize(inp):
        sent_str = sentence
        # print(sent_str)

        sentence = tokenize(sentence)

        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        # -------------------------------------------------------------------

        ans = ""
        # bol = False
        if prob.item() > 0.50:
            # print("You said sent: ",sentence)
            # print("You said str: ",sent_str)
            # print("Intents: ", intents['intents'])
            # print(type(intents['intents']))
            for intent in intents['intents']:
                if intent["tag"] == tag:
                    # responses = tag['responses']
                    responses = intent['responses']
                    # ans += random.choice(responses)

                    for key in mapping.keys():
                        # if bol == True:
                        #     break
                        if key == tag:
                            # print("inside")
                            # get_clean_data(sent_str)
                            ans += mapping.get(key)(sent_str)
                            # bol = True
                            # if bol == False:
                    else:
                        ans += random.choice(responses)
                        # bol = True

        else:
            ask = input("I think, I know something about it should i show? (Y/n)")

            if ("y" in ask) or ("Y" in ask):
                wiki(sent_str)
                ans += "Here we Go...!"
                # print(ans)
                # print("2")
            else:
                ans += "okay"
                # print(ans)
                # print("3")
        reply += str(ans) + ", "
    res = str(reply)
    print(res)
    speak(res)


# --------------------------------------------------- Main function ----------------------------------------------------#

def start_chat():
    print("Starting...")
    speak("Starting...")
    while True:
        chat()


if __name__ == "__main__":
    start_chat()

"""
GENERAL TIME TAKEN BY GRACE:

Execution time:  0.01603221893310547
Total time with hello:  7.238661766052246

Execution time:  0.0
Total time with hello:  7.178621768951416

Execution time:  1.5458641052246094
Total time with hello:  7.449854135513306

Execution time:  1.6758720874786377
Total time with hello:  8.529506206512451

Execution time:  3.908010721206665
Total time with hello:  10.346375226974487

Execution time:  2.296583414077759
Total time with hello:  9.038659811019897

Execution time:  1.3479893207550049
Total time with hello:  7.961965322494507

Execution time:  1.4101145267486572
Total time with hello:  8.561813592910767

Execution time:  0.20402169227600098
Total time with hello:  7.394111394882202
"""
