#This is a program to prcoess test scores from a file

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
    return grades


def process_file(grades):
    numbers = []
    for each in grades:
        numbers.append(each[1])
    return numbers


def process_high(numbers):


def process_low(numbers):


def process_average(numbers):


def output_scores(numbers, best, worst, middlest)


def main():
    grades = input_file()
    numbers = process_file(grades)
    best = process_high(numbers)
    worst = process_low(numbers)
    middlest = process_average(numbers)
    output_scores(numbers, best, worst, middlest


main()
