# This is an automated Monty Hall problem solver


import random


def hide_prize(doors):
    prize = random.choice(doors)
    return prize


def generate_choice(doors):
    choice = random.choice(doors)
    return choice


def test_samples1():
    winners1 = 0
    doors1 = ["door 1", "door 2", "door 3"]
    for count1 in range(0, 100, 1):
        prize = hide_prize(doors1)
        choice = generate_choice(doors1)
        if prize is choice:
            winners1 += 1
    scoreboard = [winners1]
    return scoreboard


def test_samples2(scoreboard):
    winners2 = 0
    doors2 = ["door 1", "door 2", "door 3"]
    for count in range(0, 100, 1):
        prize = hide_prize(doors2)
        choice = generate_choice(doors2)
        if doors2[0] is not prize and doors2[0] is not choice:
            if choice is doors2[1]:
                choice = doors2[2]
            else:
                choice = doors2[1]
        elif doors2[1] is not prize and doors2[1] is not choice:
            if choice is doors2[0]:
                choice = doors2[2]
            else:
                choice = doors2[0]
        else:
            if choice is doors2[0]:
                choice = doors2[1]
            else:
                choice = doors2[0]
        if prize is choice:
            winners2 += 1
    scoreboard.append(winners2)
    return scoreboard


def output_results(scoreboard):
    print("The computer initially picked the correct door:")
    print(scoreboard[0], " times out of 100.")
    print("By swapping after a goat is eliminated," +
          " the correct door is picked:")
    print(scoreboard[1], " times out of 100.")


def main():
    scoreboard = test_samples1()
    scoreboard = test_samples2(scoreboard)
    output_results(scoreboard)


main()
