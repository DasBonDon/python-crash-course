# 10-1 Learning Python
from pathlib import Path

print("\n--- Printing by reading the entire file")
path = Path('Chapter 10/learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines in a list")
lines = contents.splitlines()
for line in lines:
    print(line)