import math
import random

randValue = random.randint(1, 10000)  # Generates a random value between 1 and 10,000 to guess for
gTry = 0  # Placeholder for the amount of tries


def guess(x):
    print(f"You guessed {x}!\n")
    if int(x) == randValue:  # Checks if guess was correct
        print(f"You guessed the correct number, {x}, in {gTry} amount of tries.")
        exit()  # Stops script
    else:
        if int(x) < int(randValue):  # Checks if guess value needs to be higher/lower
            tip = "Higher"
        else:
            tip = "Lower"
        print(f"Try again! Tries : {gTry} | Hint: {tip}")


# Introduction to the game

print("Welcome to the activity challenge game \nmade by Sharman. In this game, you will \nhave to guess a random integer from \n1 to 10,000. In between your random \nguesses however, you will be provided \nmany hints to guess higher up or lower \nuntil you get it. Try and take the \nleast amount of tries as possible.\n")

while True:  # Makes sure the process is repeatable if guessed wrong
    inputVal = input('Guess a random number!\n\n')
    gTry += 1  # Adds 1 to the total tries counter
    math.trunc(int(inputVal))  # Returns the integer part of the value
    guess(inputVal)
