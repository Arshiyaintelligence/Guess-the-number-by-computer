import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number:
            print('Sorry,guess number Too low')
        elif guess > random_number:
            print('Sorry,guess number Too high')

    print(f'Yep ! You have guessed {random_number}. Congrats sarina')


guess(1000)

