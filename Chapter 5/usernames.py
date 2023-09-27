#5-10 Checking Usernames
current_users = ['kevin', 'madi', 'ethan', 'josh', 'hunter']
new_users = ['kevin', 'madi', 'ethan', 'kian', 'rinalds']

for user in new_users:
    if user.lower() in (name.lower() for name in current_users):
        print("That username is unavailable.")
    else:
        print("That username is available.")