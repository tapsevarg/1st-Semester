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

def processAverage(total, students):
    average = float(total) / students
    print("The class average is " + str(average) + ".")
    
    return average

# Main
# This is a program to automate averaging student's exam scores.
students = inputStudents()
total = inputScores(students)
processAverage(total, students)
