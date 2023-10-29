# 10-12 Favorite Number Remembered
from pathlib import Path
import json

path = Path('numbers.json')

if path.exists():
    contents = path.read_text()
    numbers = json.loads(contents)
    print(f"I know your favorite number! It's {numbers}.")
else:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("I'll remember your favorite number for next time.")