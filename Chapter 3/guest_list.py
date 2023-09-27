# 3-4 Guest List
guest_list = ['Fred Rogers', 'Winston Churchill', 'Stephen Hawking']
message = "Would you like to come to my dinner party,"
print(message , guest_list[0] + "?")
print(message , guest_list[1] + "?")
print(f"Would you like to come to my dinner party, {guest_list[2]}?")

#3-5 Changing Guest List
print(f"\nUnfortunately, {guest_list[2]} cannot make it to the party.")
guest_list.remove('Stephen Hawking')
guest_list.append('Wolfgang Amadeus Mozart')
print(message , guest_list[0] + "?")
print(message , guest_list[1] + "?")
print(f"Would you like to come to my dinner party, {guest_list[2]}?")

#3-6 More Guests
print("\nI have discovered a larger table we can use!")
guest_list.insert(0, 'George Marshall')
guest_list.insert(2, 'Walt Disney')
guest_list.append('George Lucas')
print(message , guest_list[0] + "?")
print(message , guest_list[1] + "?")
print(message , guest_list[2] + "?")
print(message , guest_list[3] + "?")
print(message , guest_list[4] + "?")
print(message , guest_list[5] + "?")

#3-7 Shrinking Guest List
print("Unfortunately, our table has shrunk. I can only invite two people.")
last_guest = guest_list.pop(-1)
print(f"Sorry, {last_guest} you're not invited.")
last_guest = guest_list.pop(-1)
print(f"Sorry, {last_guest} you're not invited.")
last_guest = guest_list.pop(-1)
print(f"Sorry, {last_guest} you're not invited.")
last_guest = guest_list.pop(-1)
print(f"Sorry, {last_guest} you're not invited.")
print(f"{guest_list[0]}, you're invited to my dinner party!")
print(f"{guest_list[1]}, you're invited to my dinner party!")
del guest_list[0]
del guest_list[0]
print(guest_list)

#3-9 Dinner Guests
print(len(guest_list))