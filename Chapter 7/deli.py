# 7-8 Deli
sandwich_orders = ['bologna', 'roast beef', 'chicken', 'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nI have made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())