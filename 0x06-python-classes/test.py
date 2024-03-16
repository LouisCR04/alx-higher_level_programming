#!/usr/bin/python3

Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

s1 = Square(3)
s2 = Square(3)
print(s1 == s2)

s1 = Square(4)
s2 = Square(3)
print(s1 > s2)
print(s1 >= s2)
print(s1 < s2)
print(s1 <= s2)
