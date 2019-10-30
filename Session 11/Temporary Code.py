# This is an automated Monty Hall problem solver


import random


def build_doors():
    doors = ["door 1", "door 2", "door 3"]
    print(doors)
    return doors
    
    
def hide_prize(doors):
    prize = random.choice(doors)
    print(prize)
    return prize


def generate_choice(doors):
    choice = random.choice(doors)
    print(choice)
    return choice


def test_samples1():
    winners1 = 0
    for count1 in range(0, 100, 1):
        doors = build_doors()
        prize = hide_prize(doors)
        choice = generate_choice(doors)
        if prize is choice:
            winners1 += 1
    print("The computer initially picked the correct door:")
    print(winners1, " times.")

    
def test_samples2():
    winners2 = 0
    for count in range(0, 100, 1):
        doors = build_doors()
        prize = hide_prize(doors)
        choice = generate_choice(doors)
        if not prize or choice:
            print


def main():
    test_samples1()
    test_samples2()

main()
