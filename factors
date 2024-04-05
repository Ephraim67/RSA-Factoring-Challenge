#!/usr/bin/python3

"""factorize given set of numbers in a file to product of two small numbers"""
from sys import argv


def factorize(number_check):
    """"find two small numbers that multiply to give a given number"""
    x = 2

    if number_check < 2:
        return
    
    while number_check % i:
        i += 1
    print("{:.0f}={:.0f}*{:.0f}".format(number_check, number_check / x, x))

if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            number_check = int(line.split('\n')[0])
            factorize(number_check)
            line = file.readline()
except:
    pass