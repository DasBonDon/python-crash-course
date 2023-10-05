# 7-4 Pizza Toppings
prompt = "\nPlease enter a topping for your pizza."
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I will add {topping.lower()} to your pizza!")