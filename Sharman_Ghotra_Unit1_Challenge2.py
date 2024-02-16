import random


def define(x):
    if x == 1:
        return "Rock"
    elif x == 2:
        return "Paper"
    elif x == 3:
        return "Scissors"


def result(x):
    print(f'Computer {x}\n')
    if x == 'Lost':
        print('You Won! Good Job!\n\n')
        exit


def rps(x):
    seed = random.randint(1, 3)
    if x == 'R':
        z = 1
    elif x == 'P':
        z = 2
    elif x == 'S':
        z = 3
    print(f"Computer picked : {define(seed)}\n")
    if seed == z:
        result('Tied')
    elif seed == 1 and z == 3:
        result('Won')
    elif seed == 1 and z == 2:
        result('Lost')
    elif seed == 2 and z == 3:
        result('Lost')
    elif seed == 2 and z == 1:
        result('Won')
    elif seed == 3 and z == 2:
        result('Won')
    elif seed == 3 and z == 1:
        result('Lost')


while True:
    x = input('Rock, Paper, or Scissors?\n')
    rps(x[0])
