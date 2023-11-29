# 10-6 Addition
print("Give me two numbers, and I'll add them!")
print("Type 'quit' to exit.")

while True:
    num_1 = input("\nFirst Number: ")
    if num_1 == 'quit':
        break
    num_2 = input("\nSecond Number: ")
    if num_2 == 'quit':
        break
    try:
        answer = int(num_1) + int(num_2)
    except ValueError:
        print("You didn't provide two numbers!")
    else:
        print(answer)