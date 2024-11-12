#7/10
from pathlib import Path 

path = Path('learning_python.txt')
content = path.read_text()
lines = content.splitlines()

stuff = ''
for line in lines:
    print(line.replace ("Python","C++"))
   
    
   


