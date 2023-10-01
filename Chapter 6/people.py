# 6-7 People
people = []

person = {'first_name': 'George', 'last_name': 'Marshall',
             'age': 35, 'city': 'San Francisco'}
people.append(person)

person = {'first_name': 'Alexander', 'last_name': 'Kozak', 
          'age': 28, 'city': 'Kiev'}
people.append(person)

person = {'first_name': 'William', 'last_name': 'Monroe',
           'age': 25, 'city': 'Houston'}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name} is from {city} and is {age} years old.")