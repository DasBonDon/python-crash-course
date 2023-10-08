# 7-9 No Pastrami
sandwich_orders = ['bologna', 'pastrami', 'roast beef', 'pastrami', 'chicken', 'pastrami', 'ham', 'turkey']
finished_sandwiches = []

print("The deli has run out of pastrami for today.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nI have made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())