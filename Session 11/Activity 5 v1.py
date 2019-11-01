# This is an automated Monty Hall problem solver


import random


def hide_prize(doors):
    prize = random.choice(doors)
    return prize


def input_guess():
    print("Try to win the car and avoid the goats!")
    print("Select between doors 1, 2, and 3 to find the hidden car.")
    print("Enter your number selection and press enter.")
    guess = input()
    while(guess != "1" and guess != "2" and guess != "3"):
        print("Valid choices are 1 through 3, then hit enter.")
        guess = input()
    guess = int(guess) - 1
    return guess


def test_samples1(guess):
    winners1 = 0
    doors1 = ["door 1", "door 2", "door 3"]
    guess = doors1[guess]
    for count1 in range(0, 100, 1):
        prize = hide_prize(doors1)
        if prize is guess:
            winners1 += 1
    return winners1


def input_switch():
    print("I'll eliminate one of the doors with a goat behind it.")
    print("Would you like to keep your original choice or switch?")
    print("Press the S button to switch")
    print("or hit enter key to keep original choice.")
    switch = input()
    while(switch != "S" and switch != "s" and switch != ""):
        print("Please choose valid option.")
        switch = input()
    if switch == "S" or switch == "s":
        choice = 1
    else:
        choice = 0
    return choice


def output_stand(winners1):
    print("You picked the correct door:")
    print(winners1, " times out of 100.")


def test_samples2(guess):
    winners2 = 0
    doors2 = ["door 1", "door 2", "door 3"]
    guess = doors2[guess]
    for count in range(0, 100, 1):
        prize = hide_prize(doors2)
        if doors2[0] is not prize and doors2[0] is not guess:
            if guess is doors2[1]:
                guess = doors2[2]
            else:
                guess = doors2[1]
        elif doors2[1] is not prize and doors2[1] is not guess:
            if guess is doors2[0]:
                guess = doors2[2]
            else:
                guess = doors2[0]
        else:
            if guess is doors2[0]:
                guess = doors2[1]
            else:
                guess = doors2[0]
        if prize is guess:
            winners2 += 1
    return winners2


def output_switch(winners2):
    print("By swapping after a goat is eliminated," +
          " the correct door is picked:")
    print(winners2, " times out of 100.")


def main():
    guess = input_guess()
    winners1 = test_samples1(guess)
    choice = input_switch()
    if choice == 0:
        output_stand(winners1)
    else:
        winners2 = test_samples2(guess)
        output_switch(winners2)


main()
