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
    print(grades)

def process_file(grades):
    
    count = 0
    for 

grades = input_file()
process_file(grades)
