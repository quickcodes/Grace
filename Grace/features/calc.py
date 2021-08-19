# ---------------------------------------------------- Mathemetics -----------------------------------------------------#

from functools import reduce
import re


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
