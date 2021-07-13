import requests, time
import pyttsx3  # voice setup

# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[6].id)  # total 5(0-4) voices are available


# # SPEAK
def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()


def weather(city):
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
    weather3 = " The Minimum Temperature you notice is " + str(min_temp) + " And. The Maximum you get is " + str(max_temp)
    weather4 = f" In Our city Air is going. At the speed of " + str(wind_speed) + " Kilometer PerHour "
    weather5 = " I Notice that. Today Sunrises " + str(sunrise) + " And goes down mean Sunset is almost " + str(sunset)
    weather6 = " And the Pressure is in the Air is " + str(pressure) + " Or Humidity in the atmosphere is " + str(humidity) + "%"
    weather7 = " Hopefully you enjoying your day. "

    speak(weather1)
    speak(weather2)
    speak(weather3)
    speak(weather4)
    speak(weather5)
    speak(weather6)
    speak(weather7)
