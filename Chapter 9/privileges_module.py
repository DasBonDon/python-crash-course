# Module for 9-12
from user_module import User

class Admin(User):
    def __init__(self, first_name, last_name, username, location):
        super().__init__(first_name, last_name, username, location)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can mute user', 'can warn user']
        
    def show_privileges(self):
        print(f"\nList of administrative privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")