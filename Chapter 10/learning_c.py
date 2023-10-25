# 10-2 Learning C
from pathlib import Path

path = Path('Chapter 10/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line.replace('Python', 'C'))