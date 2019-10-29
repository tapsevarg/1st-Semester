# This program is a Monty Hall problem simulator


def input_guess():
    print("Try to win the car and avoid the goats!")
    print("Select between doors 1, 2, and 3 to find the hidden car.")
    print("Enter your number selection and press enter.")
    guess = input()
    while(guess != "1" and guess != "2" and guess != "3"):
        print("Valid choices are 1 through 3, then hit enter.")
        guess = input()
    return guess


def process_doors(guess):
    import random
    cars = [random.randint(1, 3) for tests in range(101)]
    matches = cars.count(int(guess))
    return matches


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


def output_results(matches, choice):
    if choice == 0:
        print("You picked the correct door:")
        print(matches, "times out of 100 chances.")
    else:
        print("By switching, your choice matched the correct door")
        print((100 - matches), "times out of 100 chances.")


def main():
    guess = input_guess()
    matches = process_doors(guess)
    choice = input_switch()
    output_results(matches, choice)


main()
