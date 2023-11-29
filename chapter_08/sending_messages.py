# 8-10 Sending Messages
unsent_messages = ['Hello.', 'How are you?', 
                   'Do you want to go to the movies?']
sent_messages = []

def show_messages(messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(current_message)
        sent_messages.append(current_message)

show_messages(unsent_messages)

print(unsent_messages)
print(sent_messages)