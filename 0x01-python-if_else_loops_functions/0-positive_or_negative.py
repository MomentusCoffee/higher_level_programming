#!/usr/bin/python3
"""a program that assigns a random signed number to the variable number each time it is executed
and prints whether is it positive or negative.
"""
import random
number = random.randint(-10, 10)

if number > 0:
    print("{:d} {}".format(number, "is positive"))
elif number == 0:
    print("{:d} {}".format(number, "is zero"))
else:
    print("{:d} {}".format(number, "is negative"))
