# 7-10 Dream Vacation
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like another person to respond? (Y/N) ")
    if repeat == 'N':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s dream vacation is {response}!")