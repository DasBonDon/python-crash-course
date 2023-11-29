# 7-6 Three Exits
prompt = "\nPlease enter a topping for your pizza."
prompt += "\n(Enter 'quit' when you are finished.) "

toppings = 0
active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        break
    elif toppings == 5:
        print("You've reached the maximum amount of toppings.")
        active = False
    else:
        print(f"I will add {topping.lower()} to your pizza!")

    toppings += 1