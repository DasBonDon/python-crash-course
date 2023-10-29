# 10-11 Favorite Number
from pathlib import Path
import json

number = input("What's your favorite number? ")

path = Path('numbers.json')
contents = json.dumps(number)
path.write_text(contents)