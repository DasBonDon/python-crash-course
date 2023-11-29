# 9-13 Dice
from random import randint

class Die:
    # Create the die that can be rolled

    def __init__(self, sides=6):
        # Initialize the die
        self.sides = sides

    def roll_die(self):
        # Return a number between 1 and the number of sides
        return randint(1, self.sides)

# Make the 6-sided die and roll it 10 times
d6 = Die()

results = []
for roll in range(10):
    result = d6.roll_die()
    results.append(result)

print("Listing out 10 rolls of a d6:")
print(results)

# Make the 10-sided die and roll it 10 times
d10 = Die(sides=10)

results = []
for roll in range(10):
    result = d10.roll_die()
    results.append(result)

print("\nListing out 10 rolls of a d10:")
print(results)

# Make the 20-sided die and roll it 10 times
d20 = Die(sides=20)

results = []
for roll in range(10):
    result = d20.roll_die()
    results.append(result)

print("\nListing out 10 rolls of a d20:")
print(results)