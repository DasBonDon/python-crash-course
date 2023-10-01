# 6-8 Pets

pets = []

pet = {
    'name': 'bean',
    'type': 'cat',
    'owner': 'robert',
}
pets.append(pet)

pet = {
    'name': 'fluffy',
    'type': 'dog',
    'owner': 'dennis',
}
pets.append(pet)


pet = {
    'name': 'stuart',
    'type': 'mouse',
    'owner': 'george',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")