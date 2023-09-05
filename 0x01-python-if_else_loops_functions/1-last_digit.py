#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dig = number % 10
if l_dig > 5:
    string = "greater than 5"
elif l_dig == 0:
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"
print(f"Last digit of {number} is {l_dig} and is {string}")
