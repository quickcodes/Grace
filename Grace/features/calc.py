# ---------------------------------------------------- Mathemetics -----------------------------------------------------#

from functools import reduce
import re
# -----------------------------------------------------------------------------------------------------------
import asyncio # Multiprocessing 
# -----------------------------------------------------------------------------------------------------------

async def add(inp):
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x + y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


async def sub(inp):
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x - y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


async def mul(inp):
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x * y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


async def power(inp):
    try:
        numbers = re.findall('\d+', inp)
        numbers = list(map(int, numbers))
        sum = reduce(lambda x, y: x ** y, numbers)
        return "Its " + str(sum)
    except:
        return "Something went wrong."


async def div(inp):
    try:
        numbers = re.findall('\d+', inp)
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        ans = numbers[0] / numbers[1]
        return "Its " + str(ans)
    except:
        return "Something went wrong"
