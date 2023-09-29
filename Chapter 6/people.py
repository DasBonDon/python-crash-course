# 6-7 People
people = {
    'gmarshall': {
        'first_name': 'George', 
        'last_name': 'Marshall',
        'age': 35,
        'city': 'San Francisco',
    },

    'akozak': {
        'first_name': 'Alexander',
        'last_name': 'Kozak',
        'age': 28,
        'city': 'Kiev',
    },

    'wmonroe': {
        'first_name': 'William',
        'last_name': 'Monroe',
        'age': 25,
        'city': 'Houston',
    },

}

for k, v in people.items():
    print(f"\nFirst Name: {v['first_name']}")
    print(f"Last Name: {v['last_name']}")
    print(f"Age: {v['age']}")
    print(f"City: {v['city']}")