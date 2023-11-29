# 6-10 Favorite Numbers
favorite_numbers = {
    'kevin': ['42', '44'],
    'madi': ['7', '55'],
    'ethan': ['27', '84'],
    'josh': ['60', '77'],
    'hunter': ['30', '50'],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
