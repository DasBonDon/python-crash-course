#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())