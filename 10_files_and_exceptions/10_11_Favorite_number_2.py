#7/10

import json
from pathlib import Path

path = Path('fav_numbers.json')

if path.exists():
    with path.open('r') as f:
        fav_number = json.load(f)
        print(f"Your favorite number is {fav_number}")
else:
    print("Your favorite number is not found.")