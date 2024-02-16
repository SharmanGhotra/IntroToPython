import random

def calcRand():
    y = random.randint(1, 100) #Generates a random integer between 1 and 100
    z = int(x) * int(y) #Multiplies the input integer by the random integer
    print(f"{z} is your final number. It was reached using {x} multiplied by {y}")





while True:
    #Asks for a integer to start the function
    x = input("Enter in a integer to be multiplied by a random integer from 1 to 100. - ")
    calcRand() #Call on the function

