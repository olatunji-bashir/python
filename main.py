
import random


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' fpr scissors:")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'you won'

    return 'you lost'


# r > s, s > p, p > r


print(play())
