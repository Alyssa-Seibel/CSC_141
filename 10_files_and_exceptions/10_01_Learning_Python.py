# 6/10
from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print(content)
print("------------------")

lines = content.splitlines()
for line in lines:
    print(line)


