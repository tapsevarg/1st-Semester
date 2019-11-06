# This is an automated number guesser


def input_start():
    while True:
        print("Think of a number between 0-100, then press enter")
        start = input()
        if not(start != ""):
            break


def process_guess():
    history = []
    low = 0
    high = 100
    while True:
        guess = (low + high) // 2
        history.append(guess)
        print("Is your number " + str(guess) + "?")
        print("Press 'H' key if your number is higher")
        print("Press 'L' key if your number is lower")
        print("Press 'E' key if I guessed your number correctly")
        response = input()
        if response == "E" or response == "e":
            break
        elif response == "H" or response == "h":
            low = guess + 1
        elif response == "L" or response == "l":
            high = guess - 1
        else:
            print("Let's try again")
    return history


def output_results(history):
    print("It took me " + str(len(history)) +
          " attempts to guess your number.")
    print("Here were my guesses: " + str(history)[1: -1] + ".")


def main():
    input_start()
    history = process_guess()
    output_results(history)


main()
