# 5/10
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
for lines in contents.splitlines():
 print(lines)