# This is a grade averager


def input_scores():
    print("Input each grade and press enter")
    print("Just press enter when finished")
    total = 0
    count = -1
    while True:
        count += 1
        student = input()
        try:
            student = int(student)
        except ValueError:
            break
        total = total + int(student)
    average = total / count
    return average


def output_scores(average):
    print("The average score is " + str(average) + ".")


def main():
    average = input_scores()
    output_scores(average)


main()
