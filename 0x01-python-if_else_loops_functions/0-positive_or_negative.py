#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    signage = "negative"
elif number > 0:
    signage = "positive"
else:
    signage = "zero"
print(f"{number} is {signage}")
