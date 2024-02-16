import random



def bingo():
    balls = {
        'B': list(range(7, 14)),
        'I': list(range(21, 28)),
        'N': list(range(35, 42)),
        'G': list(range(49, 56)),
        'O': list(range(63, 70))
    }

    while balls:
        letter = random.choice(list(balls.keys()))
        number = random.choice(balls[letter])
        balls[letter].remove(number)  # Remove number from letter list
        if not balls[letter]:  # Letter has no more numbers
            print('Removing', letter)
            del balls[letter]  # Delete letter from dictionary
        yield(letter, number)


def main():
    for ball in bingo():
        print(f'\n{ball}')
        if input('Enter for next ball or q to quit ') == 'q':
            print('Congratulations!')
            break
    else:
        print('All out of balls.')


def letter(z):
    return lettersList[z]  # Function to return letter for each row


lettersList = ['', 'B', 'I', 'N', 'G', 'O']

card_list = []
print('Your Bingo Card -\n')
for num in range(1, 6):
    y = num * 14  # Sets ceiling for the random bingo card
    for num2 in range(5):
        x = random.randint(y / 2, y)  # Gets number for card in each columm and row
        if x in card_list:
            x = random.randint(y / 2, y+1)  # Gets rid of high possibility of repeats
        card_list.append(x)
    print(f'{letter(num)} {card_list}')  # Returns bingo card
    card_list = []  # Clears list


main()
