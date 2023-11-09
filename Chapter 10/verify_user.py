# 10-14 Verify User
from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username 

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        confirm = input(f"Are you {username}? ").lower()
        if confirm in ['yes', 'y']:
            print(f"Welcome back, {username}!")
            return
        
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")

greet_user()