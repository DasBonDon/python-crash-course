#2-7 Stripping Names
name = " kevin "
# \n creates a new line while \t creates an indentation. The strip function is taking away the spaces on either side of the name variable.
print(name, '\n', name.lstrip(), '\n\t', name.rstrip(), '\n', name.strip())