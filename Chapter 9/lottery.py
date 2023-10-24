# 9-14 Lottery
from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winner = []
print("Let's find out whose gonna win!")

while len(winner) < 4:
    pull = choice(list)

    if pull not in winner:
        print(f"\tThere's a {pull}!")
        winner.append(pull)

print(f"\nThe winning ticket is: {winner}")