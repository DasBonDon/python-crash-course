# Reader for 10-11 Favorite Number
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(f"I know your favorite number! It's {numbers}.")