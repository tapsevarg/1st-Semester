def inputIterations():
    print("How many iterations of Pi would you like me to calculate?")
    iterations = int(input())
    
    return iterations

def outputNilakantha():
    print("Have a nice day!")

def processNilakantha(iterations):
    count = 1
    factorA = 0
    factorB = 1
    factorC = 2
    nilakantha = 3
    print(nilakantha)
    for count in range(2, iterations + 1, 1):
        factorA = factorA + 2
        factorB = factorB + 2
        factorC = factorC + 2
        factors = factorA * factorB * factorC
        if count % 2 < 1:
            nilakantha = nilakantha + 4 / factors
            print(nilakantha)
        else:
            nilakantha = nilakantha - 4 / factors
            print(nilakantha)

# Main
# This is a Nilakantha Pi calculator
iterations = inputIterations()
processNilakantha(iterations)
outputNilakantha()
