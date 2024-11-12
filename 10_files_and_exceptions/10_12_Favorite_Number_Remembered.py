from pathlib import Path
import json

def get_stored_username(path):
    '''store the info'''
    if path.exists():
        content = path.read_text()
        return json.loads(content)
    return None
    
def greet_user():
    '''Greet the user with their fav number'''
    path = Path('favorite_number.json')
    number = get_stored_username(path)    
    if number:
        print(f"Your favorite number is {number}!")
    else:
        number = input("What is your favorite number? ")
        path.write_text(json.dumps(number))
        print(f"We will remember your favorite number for the future.")

greet_user()