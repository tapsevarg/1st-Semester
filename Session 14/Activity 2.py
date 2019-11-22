# This is a program to process test scores from a file
# with built in error handling.

import os.path
from os import path
import sys


def input_file():
    grades = []
    try:
        with open("scores.txt", "r") as file:
            next(file)
            for line in file:
                line = line.strip()
                grades.append(line)
    except:
        print("Error reading scores.txt")
        print(sys.exc_info()[1])
    for index in grades:
        index = index.strip()
        index = index.replace(",", " ")
        print(index)
    return grades


def process_file(grades):
    numbers = []
    for each in grades:
        each = each.split(",")
        try:
            numbers.append(each[1])
        except:
            print("Error with formatting")
            print(sys.exc_info()[1])
            sys.exit()
        try:
            numbers = [int(convert) for convert in numbers]
        except:
            print("Expected score value is not numeric")
            print(sys.exc_info()[1])
            sys.exit()
    return numbers


def process_high(numbers):
    maximum = max(numbers)
    return maximum


def process_low(numbers):
    minimum = min(numbers)
    return minimum


def process_average(numbers):
    middle = sum(numbers) / len(numbers)
    middle = round(middle, 2)
    return middle


def output_scores(grades, maximum, minimum, middle):
    print("The highest score was " + str(maximum) + ".")
    print("The lowest score was " + str(minimum) + ".")
    print("The class average was " + str(middle) + ".")


def main():
    if path.exists("scores.txt") and os.path.getsize("scores.txt") > 0:
        grades = input_file()
        numbers = process_file(grades)
        maximum = process_high(numbers)
        minimum = process_low(numbers)
        middle = process_average(numbers)
        output_scores(grades, maximum, minimum, middle)
    else:
        print("Error finding file or file is empty")


main()
