#4-1 Pizzas
pizzas = ['pineapple', 'cheese', 'sausage']
for pizza in pizzas:
    print(f"I love {pizza} pizza!")
print("\nPizza is the greatest food ever made!")

#4-10 Slices
print("\nThe first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza.title())

pizzas.append('pepperoni')
pizzas.append('tomato')

print("\nThree items from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza.title())

print("\nThe last three items in the list are:")
for pizza in pizzas[2:]:
    print(pizza.title())

#4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('mushroom')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())