#2/10
from pathlib import Path
import json

fav_number = input("What is your favorite number? ")

path = Path('fav_numbers.json')

with path.open('w') as f:
    json.dump(fav_number,f)
    print("Your favorite number has been saved!")
