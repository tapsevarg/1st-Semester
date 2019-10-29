# This is an automatic Monty Hall problem solver

import random
goat = 0
car = 1


def build_doors():
    doors = [0, 1, 0]
    random.shuffle(doors)
    return doors


def generate_choice(doors):
    choice = random.choice(doors)
    return choice


def process_game(doors, choice):
    scorecard[0, 2]
    if choice == index.doors:
        winner +=1
    else:
        loser +=1

        
doors = build_doors()
choice = generate_choice(doors)
scorecard = process_game(doors, choice)
