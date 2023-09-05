#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dig = abs(number) % 10
if l_dig > 5 and number > 0:
    string = " and is greater than 5"
elif l_dig == 0:
    string = " and is 0"
else:
    string = " and is less than 6 and not 0"
if number > -1 or l_dig == 0:
    print(f"Last digit of {number} is {l_dig}{string}")
else:
    print(f"Last digit of {number} is -{l_dig}{string}")
