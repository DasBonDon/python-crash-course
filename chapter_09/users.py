# 9-3 Users
class User:
    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.location = location.title()

    def describe_user(self):
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Location: {self.location}")
        
    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

user = User('George', 'Marshall', 'gmarsh', 'United States')
user.describe_user()
user.greet_user()

user = User('Thomas', 'Jefferson', 'tjeff', 'United States')
user.describe_user()
user.greet_user()

user = User('Josip', 'Broz', 'tito', 'Yugoslavia')
user.describe_user()
user.greet_user()