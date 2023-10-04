# 7-2 Restaurant Seating
seats = input("How many people are in your dinner group? ")
seats = int(seats)

if seats > 8:
    print("You'll have to wait for a table to be ready.")
else:
    print("Your table is ready for you.")