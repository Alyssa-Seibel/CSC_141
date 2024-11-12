from pathlib import Path
import json

def get_stored_username(path):
    '''get user if available'''
    if path.exists():
        content = path.read_text()
        username = json.loads(content)
        return username
    else:
        return None
    
def get_new_username(path):
    '''Prompt for new user'''
    username = input("What is your name? ")
    content = json.dumps(username)
    path.write_text(content)
    return username

def greet_user():
    '''greet user'''
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}")
        else:
            username = get_new_username(path)
            print(f"We will remember you for next time, {username}")

    else:
        username = get_new_username(path)
        print(f"We will remember you for next time, {username}")

greet_user()