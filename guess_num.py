import random

def guess(x):
    random_number = random.randint(0, x)
    guess = -1
    while guess !=random_number:
        guess = int(input(f"Guess a number between 0 and {x}:"))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")

    print("Correct, congrats, you got it!")

guess(10)