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
    return winners1


def implement_switch(prize, choice, doors):
    if not prize or choice:
        del [doors]
    

def test_samples2():
    winners2 = 0
    for count2 in range(0, 100, 1):
        doors = build_doors()
        prize = hide_prize(doors)
        choice = generate_choice(doors)
        switch = implement_switch(prize, choice, doors)
        if prize is switch:
            winners2 += 1
    return winners2

def ouput_results(winners1, winners2):
    print("The computer initially picked the correct door:")
    print(winners1, " times.")
    print("By switching, the computer picked the correct door:")
    print(winners2)


def main():
    test_samples1()
    test_samples2()
    output_result(winners1, winners2)

main()
