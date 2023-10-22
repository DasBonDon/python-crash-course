# Module for 9-12
class User:
    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Location: {self.location}")
        
    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0