def main():
    age = int(input('How old are you?\n'))

    if age >= 60:
        print('You can enter into the lottery in any state, but you shouldn''t need to.')
    elif age >= 21:
        print('You can enter into the lottery in any state.')
    elif age >= 18:
        print('Sorry, you can''t enter into the lottery in some states.')
    else:
        print('Sorry, you can''t enter into the lottery in ANY state.')


main()
