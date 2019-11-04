# This is an automated number guesser


def input_start():
    while True:
        print("Think of a number between 0-100, then press enter")
        start = input()
        if not(start != ""):
            break


def process_guess():
    history = []
    guess = 50
    bouncer = 25
    while True:
        guess = min(max(guess, 0), 100)
        bouncer = min(max(bouncer, 1), 100)
        print("Is your number " + str(guess) + "?")
        print("Press 'H' key if your number is higher")
        print("Press 'L' key if your number is lower")
        print("Press 'E' key if I guessed your number correctly")
        response = input()
        if response == "E" or response == "e":
            history.append(guess)
            break
        elif response == "H" or response == "h":
            history.append(guess)
            guess = int(guess + bouncer)
            bouncer = (bouncer * 0.5)
        elif response == "L" or response == "l":
            history.append(guess)
            guess = int(guess - bouncer)
            bouncer = (bouncer * 0.5)
        else:
            print("Let's try again")
    return history


def output_results(history):
    print("It took me " + str(len(history)) +
          " attempts to guess your number.")


def main():
    input_start()
    history = process_guess()
    output_results(history)


main()
