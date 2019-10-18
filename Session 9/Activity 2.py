def inputStart():
    while True:    #This simulates a Do Loop
        print("Think of a number between 0-100, then press enter")
        start = input()
        if not(start != ""): break   #Exit loop

def outputResults(count):
    print("It took me " + str(count) + " attempts to guess your number.")

def processGuess():
    guess = 50
    bouncer = 25
    count = 1
    while True:    #This simulates a Do Loop
        print("Is your number " + str(guess) + "?")
        print("Press 'H' key if your number is higher")
        print("Press 'L' key if your number is lower")
        print("Press 'E' key if I guessed your number correctly")
        response = input()
        if response == "E" or response == "e":
            pass
        else:
            if response == "H" or response == "h":
                guess = guess + bouncer + 1
            else:
                if response == "L" or response == "l":
                    guess = guess - bouncer - 1
                else:
                    print("please press one of the key options")
        count = count + 1
        bouncer = int(bouncer * 0.5)
        if not(response == "H" or response == "h" or response == "L" or response == "l"): break   #Exit loop
    
    return count

# Main
inputStart()
count = processGuess()
outputResults(count)
