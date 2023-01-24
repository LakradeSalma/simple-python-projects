import random

print("Rock, Paper, Scissors")


def game():
    player = input("'r' for rock, 'p' for paper and 's' for scissors :")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return 'A tie!'

    # r > s, s > p, p >r
    if is_winner(player, computer):
        return 'You won!'

    return 'You lost!'


def is_winner(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (
            player1 == 'p' and player2 == 'r'):
        return True


print(game())
