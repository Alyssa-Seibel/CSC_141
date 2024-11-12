# 2/10
from pathlib import Path

name = input("What is your name?")
content = (name)
path = Path('guest.txt')
path.write_text(content)