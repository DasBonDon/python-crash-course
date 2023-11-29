# 9-15 Lottery Analysis
from random import choice

def get_winner(combinations):
    # Return the winning ticket from a list of numbers/letters
    winner = []

    # Keeping the length of the ticket to 4
    while len(winner) < 4:
        pull = choice(combinations)

        # Pull the item if it hasn't already been
        if pull not in winner:
            winner.append(pull)

    return winner

def check_ticket(ticket, winner):
    # Check if our ticket is a winner
    for element in ticket:
        if element not in winner:
            return False
    
    # If it is a winner, return True
    return True

def make_ticket(combinations):
    # Make a ticket
    ticket = []
    
    # Keeping the length of the ticket to 4
    while len(ticket) < 4:
        pull = choice(combinations)

        # Pull the item if it hasn't already been
        if pull not in ticket:
            ticket.append(pull)

    return ticket

combinations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winner = get_winner(combinations)

tries = 0
won = False

# Set max number of tries
max_tries = 1_000_000

while not won:
    my_ticket = make_ticket(combinations)
    won = check_ticket(my_ticket, winner)
    tries += 1
    if tries >= max_tries:
        break

if won:
    print("We have a winner!")
    print(f"Your ticket is: {my_ticket}")
    print(f"The winning ticket is: {winner}")
    print(f"It took {tries} tries to win!")
else:
    print(f"We tried {tries} times without pulling a winner.")
    print(f"Your ticket is: {my_ticket}")
    print(f"The winning ticket is: {winner}")