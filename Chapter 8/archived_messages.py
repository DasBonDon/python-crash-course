# 8-11 Archived Messages
def show_messages(messages):
    # Printing the messages in the list.
    print("Displaying text messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    # Print the messages again but move them to a new list.
    print("\nSending all text messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

# Define the lists
messages = ['Hello.', 'How are you?', 'Do you want to go to the movies?']
sent_messages = []

# Call both functions
show_messages(messages)
send_messages(messages[:], sent_messages)

print("\nLists:")
print(messages)
print(sent_messages)