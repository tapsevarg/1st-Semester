# This is a program to process test scores from a file

import os.path
from os import path
import sys


def input_file():
    grades = []
    with open("scores.txt", "r") as file:
            next(file)
            for line in file:
                line = line.strip()
                grades.append(line)
    return grades


def process_file(grades):
    numbers = []
    for each in grades:
        each = each.split(",")
        numbers.append(int(each[1]))
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
    print("The class scores were as follows:")
    for index in grades:
        index = index.strip()
        index = index.replace(",", " ")
        print(index)


def main():
    if path.exists("scores.txt"):
        grades = input_file()
        numbers = process_file(grades)
        maximum = process_high(numbers)
        minimum = process_low(numbers)
        middle = process_average(numbers)
        output_scores(grades, maximum, minimum, middle)
    else:
        print("Error finding scores.txt file")


main()
