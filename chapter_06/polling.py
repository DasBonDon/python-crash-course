#6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

people = ['jen', 'sarah', 'kevin', 'ethan', 'josh']

for person in people:
    if person in favorite_languages:
        print(f"Thank you {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, you are invited to take the poll!")