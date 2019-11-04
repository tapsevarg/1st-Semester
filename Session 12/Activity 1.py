# This is a dynamic grade averager


def input_scores():
    print("Input each grade and press enter")
    print("Just press enter when finished")
    total = 0
    count = -1
    scores = []
    while True:
        count += 1
        student = input()
        try:
            student = int(student)
        except ValueError:
            break
        scores.append(student)
    return scores
    
    
def process_average(scores):
    total = 0
    for index in range(len(scores)):
        total += scores[index]
    average = total/(len(scores))
    return average
    
    
def process_maximum(scores):
    maximum = max(scores)
    return maximum
    
    
def process_minimum(scores):
    minimum = min(scores)
    return minimum
        
        
def process_sort(scores):
    scores.sort(reverse=True)
    return scores


def output_grades(average, maximum, minimum, scores):
    print("The grades are as follows: " + str(', '.join(scores))
    print("The average score is " + str(average) + ".")
    print("The highest grade was " + str(maximum) + 
          " and the lowest was " + str(minimum) + ".")

def main():
    scores = input_scores()
    average = process_average(scores)
    maximum = process_maximum(scores)
    minimum = process_minimum(scores)
    scores = process_sort(scores)
    output_grades(average, maximum, minimum, scores)


main()
