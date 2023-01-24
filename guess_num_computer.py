import random


def computer_guess(x):
    low = 0
    high = x
    feedback = ""
    while feedback != "C":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input((f"Is {guess} correct (C), too low (L) or too high (H): ".upper()))
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1

    print(f"The computer got your number {guess}!")


your_num = input("Choose a number between 1 and 1000: ")

computer_guess(1000)
