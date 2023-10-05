# 7-5 Movie Tickets
age = input("Please enter your age to get your ticket price. ")
age = int(age)

if age < 3:
    print("Your ticket is free.")
elif age < 13:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")