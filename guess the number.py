import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0  # initate the guess variable
    while guess != random_number:
        guess = (input("input a number"))
        if guess < random_number:
            print("value is too low")
        elif guess > random_number:
            print("value is too high")
    print(f'you are right {random_number} is correct!!!!')


guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess: int = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct(C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Congrats! the computer guessed your number, {guess}, correctly')


computer_guess(10)
