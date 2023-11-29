# 10-13 User Dictionary
from pathlib import Path
import json

def get_stored_user(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    country = input("What country are you from? ")
    movie = input("What is your favorite movie? ")

    user = {
        'username': username,
        'country': country,
        'movie': movie,
    }

    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(f"\nUsername: {user['username']}")
        print(f"Country: {user['country']}")
        print(f"Favorite Movie: {user['movie']}")
    else:
        user = get_new_user(path)
        print(f"We'll remember you next time, {user['username']}!")

greet_user()