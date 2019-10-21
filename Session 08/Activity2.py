def inputScores(students):
    total = 0
    while students > 0:
        print("Enter score")
        score = int(input())
        total = total + score
        students = students - 1
    
    return total

def inputStudents():
    print("Enter total number of exams to average and press enter")
    students = int(input())
    
    return students

def outputAverage(average):
    print("The average test score is " + str(average) + ".")

def processAverage(total, students):
    average = float(total) / students
    
    return average

# Main
# This is a program to automate averaging student's exam scores.
students = inputStudents()
total = inputScores(students)
average = processAverage(total, students)
outputAverage(average)
