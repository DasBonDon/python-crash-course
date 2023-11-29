# 10-5 Guest Book
from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nWhat is your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guests = []

while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"{name}, you have been added to the guest book.")
    guests.append(name)

string = ''
for name in guests:
    string += f"{name}\n"

path.write_text(string)