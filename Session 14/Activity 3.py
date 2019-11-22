#This is a program to process HTML from a file


import os.path
from os import path
import sys


def input_file():
    print("To parse a file, please enter the filename.")
    print("Remember to include the filename extension.")
    print("(Example: information.txt)")
    name = input()
    taco = []
    if path.exists(name):
        try:
            with open(name, "r") as file:
                for tag in file:
                    tag = tag.strip()
                    taco.append(tag)
                    print(taco)
        except:
            print("Error reading file")
            print(sys.exc_info()[1])
    else:
        print("Danger")



def main():
    input_file()


