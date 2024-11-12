#
''' The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Wamerite this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.'''

from pathlib import Path
import json

def get_stored_user_info(path):
    '''get user if exists'''
    if path.exists():
        content = path.read_text()
        user_dict = json.loads(content)
        return user_dict
    else:
        return None
    
def get_new_user_info(path): 
    '''prompt new username'''
    username = input("What is your name? ")
    age = input("What is your age? ")
    color = input("What is your favorite color? ")

    user_dict = {
        'username': username,
        'age':age,
        'color':color,
    }

    content = json.dumps(user_dict)
    path.write_text(content)
    return user_dict
    
def greet_user():
    '''greet user if they exist in file'''
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"You are currently {user_dict['age']}!")
        print(f"Your favorite color is {user_dict['color']}")
    else:
        user_dict = get_new_user_info(path)
        msg = (f"We'll remember you when you come back, {user_dict['username']}!")
        print(msg)

greet_user()