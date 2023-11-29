#3-10 Every Function
languages = ['German', 'French', 'Spanish', 'English', 'Japanese']

print(languages)
print(languages[0])
print(languages[1].lower())
print(languages[-1])

message = f"I love the {languages[0]} language!"
print(message)

languages[0] = 'Russian'
print(languages)

languages.append('Korean')
print(languages)

languages.insert(0, 'Polish')
print(languages)

del languages[0]
print(languages)

popped_language = languages.pop()
print(languages)
print(popped_language)
print(f"I'm not a big fan of the {popped_language} language.")

popped_language = languages.pop(0)
print(f"I'm not a big fan of the {popped_language} language.")

languages.remove('French')
print(languages)

bad_language = 'Spanish'
languages.remove(bad_language)
print(languages)
print(f"\nI really don't like the {bad_language} language.")

languages.append('German')
languages.append('French')
languages.append('Mandarin')
print(languages)

print(sorted(languages))
print(sorted(languages, reverse=True))

languages.reverse()
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(len(languages))