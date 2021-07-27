# import random, requests
# import time
# import wikipedia
#
#
# def tell_time():
#     current_time = time.localtime()
#     hour = int(time.strftime("%H", current_time))
#     minute = int(time.strftime("%M", current_time))
#     if hour < 12:
#         # print(f"\tIts {hour} : {minute} AM")
#         tme = f"Its {hour} : {minute} AM"
#         return tme
#     else:
#         hour -= 12
#         if hour == 0:
#             hour = 12
#         tme = f"Its {hour} : {minute} AM"
#         return tme
#
#
# def wiki(inp):
#     inp = inp.replace("tell", "").replace("me", "").replace("about", "").replace("who", "").replace("is", "")
#     inp = inp.replace("what", "").replace("are", "").replace("someting", "").replace("of", "").replace("know", "")
#     inp = inp.replace("kaun h", "").replace("baare m", "").replace("batao", "").replace("of", "").replace("know", "")
#     inp = inp.replace("give me details", "").replace("jankari do", "").replace("collect information", "").replace(
#         "pata lagao", "")
#     inp = inp.replace("search", "")  # .replace("details","").replace("kaun","").replace("","").replace("know","")
#     result = wikipedia.summary(inp, sentences=1)
#     return result
#
#
# def me():
#     lst = ["Developer. Right?", "Student", "college student", "Software student...!", "Human", "Artificial Human"]
#     return random.choice(lst)
#
#
# def you():
#     lst = ["I am software engineer.", "I am currently studying. Yeah!", "I'm in university. Learning computer science.", "Mechanical engineer"]
#     return random.choice(lst)
#
# def joke():
#     json_data = requests.get("https://official-joke-api.appspot.com/random_joke").json()
#     first_line = json_data['setup']
#     punch_line = json_data['punchline']
#     # print(first_line)
#     # time.sleep(2)
#     # return punch_line
#     return str(first_line) + "\n" + str(punch_line)