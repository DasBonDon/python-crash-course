# 10-2 Learning C
from pathlib import Path

path = Path('Chapter 10/learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace('Python', 'C'))