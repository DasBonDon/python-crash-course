#5-1 Conditional Tests

#Five True Tests
topping = 'pepperoni'
print("Is topping == 'pepperoni'? I predict True.")
print(topping == 'pepperoni')

car = 'audi'
print("Is car == 'audi'? I predict True.")
print(car == 'audi')

bike = 'bmx'
print("Is bike == 'bmx'? I predict True.")
print(bike == 'bmx')

animal = 'cat'
print("Is animal == 'cat'? I predict True.")
print(animal == 'cat')

woman = 'madi'
print("Is woman == 'madi'? I predict True.")
print(woman == 'madi')

#Five False Tests
topping = 'mushroom'
print("Is topping == 'pepperoni'? I predict False.")
print(topping == 'pepperoni')

car = 'bmw'
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

bike = 'mountain'
print("Is bike == 'bmx'? I predict False.")
print(bike == 'bmx')

animal = 'dog'
print("Is animal == 'cat'? I predict False.")
print(animal == 'cat')

woman = 'karen'
print("Is woman == 'madi'? I predict False.")
print(woman == 'madi')

#5-2 More Conditional Tests
game = 'Grand Theft Auto V'
print("Is game == 'Grand Theft Auto V'? I predict True.")
print(game == 'Grand Theft Auto V')

film = 'Pulp Fiction'
print("Is film != 'Pulp Fiction'? I predict False.")
print(film != "Pulp Fiction")

food = 'Pizza'
print("Is food == 'Pizza'? I predict True.")
print(food.lower() == 'pizza')

age = 21
print("Is age greater than 21? I predict False.")
print(age > 21)

age = 21
print("Is age less than 21? I predict False.")
print(age < 21)

age = 21
print("Is age greater than or equal to 21? I predict True.")
print(age >= 21)

age = 21
print("Is age less than or equal to 21? I predict True.")
print(age <= 21)

age_01 = 21
age_02 = 19
print("Is age_01 == 21 and age_02 >= 21? I predict False.")
print(age_01 == 21 and age_02 >= 21)

age_01 = 21
age_02 = 19
print("Is age_01 == 21 or age_02 >= 21? I predict True.")
print(age_01 == 21 or age_02 >= 21)

food = ['pizza', 'sausage']
print("Is chicken in food? I predict False.")
print('chicken' in food)

food = ['pizza', 'sausage']
print("Is chicken not in food? I predict True.")
print('chicken' not in food)