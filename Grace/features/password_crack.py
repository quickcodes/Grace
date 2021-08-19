import random
import string
import time
import getpass

def lowerCase():
    lc = string.ascii_lowercase
    char_lst = list(lc)
    pswd = input("Enter the password: ")
    startTime = time.time()
    st = round(startTime, 4)
    print("Cracking...")
    guess = ""
    count = 0
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
        count += 1
    endtime = time.time()
    # et = round(endtime, 4)
    timetaken = (startTime - endtime)
    res = float(timetaken)
    print("\tIt took %.3f seconds to calculate." % res)
    print("\tpassword is: " + guess)
    print(f"\tTotal Number of Random guesses {count}")


def upperCase():
    uper = string.ascii_uppercase
    char_lst = list(uper)
    pswd = input("Enter the password: ")
    startTime = time.time()
    st = round(startTime, 4)
    print("Cracking...")
    guess = ""
    count = 0
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
        count += 1
    endtime = time.time()
    # et = round(endtime, 4)
    timetaken = (startTime - endtime)
    res = float(timetaken)
    print("\tIt took %.3f seconds to calculate." % res)
    print("\tpassword is: " + guess)
    print(f"\tTotal Number of Random guesses {count}")


def digits():
    digit = string.digits
    char_lst = list(digit)
    pswd = input("Enter the password: ")
    startTime = time.time()
    st = round(startTime, 4)
    print("Cracking...")
    guess = ""
    count = 0
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
        count += 1
    endtime = time.time()
    # et = round(endtime, 4)
    timetaken = (startTime - endtime)
    res = float(timetaken)
    print("\tIt took %.3f seconds to calculate." % res)
    print("\tpassword is: " + guess)
    print(f"\tTotal Number of Random guesses {count}")


def mixword():
    words = string.ascii_letters
    char_lst = list(words)
    pswd = input("Enter the password: ")
    startTime = time.time()
    st = round(startTime, 4)
    print("Cracking...")
    guess = ""
    count = 0
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
        count += 1
    endtime = time.time()
    # et = round(endtime, 4)
    timetaken = (startTime - endtime)
    res = float(timetaken)
    print("\tIt took %.3f seconds to calculate." % res)
    print("\tpassword is: " + guess)
    print(f"\tTotal Number of Random guesses {count}")


def wordsDigits():
    lc = string.ascii_letters
    dgt = string.digits
    char_lst = list(lc + dgt)
    pswd = input("Enter the password: ")
    startTime = time.time()
    st = round(startTime, 4)
    print("Cracking...")
    guess = ""
    count = 0
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
        count += 1
    endtime = time.time()
    # et = round(endtime, 4)
    timetaken = (startTime - endtime)
    res = float(timetaken)
    print("\tIt took %.3f seconds to calculate." % res)
    print("\tpassword is: " + guess)
    print(f"\tTotal Number of Random guesses {count}")


def fuckingCrazy():
    lc = string.printable
    char_lst = list(lc)
    pswd = input("Enter the password: ")
    startTime = time.time()
    st = round(startTime, 4)
    print("Cracking...")
    guess = ""
    count = 0
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
        count += 1
    endtime = time.time()
    # et = round(endtime, 4)
    timetaken = (startTime - endtime)
    res = float(timetaken)
    print("\tIt took %.3f seconds to calculate." % res)
    print("\tpassword is: " + guess)
    print(f"\tTotal Number of Random guesses {count}")

def main():
    end = ''
    while end != 'q':
        print()
        print("       Which type of password I want to guess")
        print('''     < Please choose the complexity of password >
            1. Lower case 
            2. Upper case
            3. Digits
            4. Mix words
            5. words and Numbers
            6. Crazy
            ''')
        try:
            num = int(input("    --> "))
            if num == 1:
                lowerCase()
            elif num == 2:
                upperCase()
            elif num == 3:
                digits()
            elif num == 4:
                mixword()
            elif num == 5:
                wordsDigits()
            elif num == 6:
                fuckingCrazy()
            else:
                print("       < Please enter valid number >")
        except:
            print("Something went wrong")
        print("\n       Press any key to play again and 'q' for exit")
        end = input("    --> ")
        if end == 'q':
            print("Bye Bye")

if __name__ == '__main__':
    main()
