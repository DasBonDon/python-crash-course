# 10-10 Common Words
from pathlib import Path

path = Path("Chapter 10/republic.txt")
contents = path.read_text(encoding='utf-8')

count = contents.lower().count('the')
print(count)

count = contents.lower().count('the ')
print(count)