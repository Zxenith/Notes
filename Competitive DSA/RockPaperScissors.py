#Rock Paper Scissors

import random

def RPS():

    print("Type 'R' for Rock, 'P' for Paper and 'S' for Scissors!")
    choose = ["R",  "P", "S"]

    a = random.choice(choose)

    b = input("Enter your selection: ")

    print(f"Computer selected: {a}")

    if a == b:
        print("It's a Draw!")

    elif a == choose[0] and b == choose[1]:
        print("You win!")

    elif a == choose[1] and b == choose[2]:
        print("You win!")

    elif a == choose[2] and b == choose[0]:
        print("You win!")

    elif b not in choose:
        print("Invalid")
        RPS()

    else:
        print("You Lose!")

RPS()
