# 10-9 Silent Cats and Dogs
from pathlib import Path

def read_path(files):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(f"\nHere are the contents of {path}: ")
        print(f"{contents}")

files = ['Chapter 10\cats.txt', 'Chapter 10\dogs.txt']
for file in files:
    path = Path(file)
    read_path(path)