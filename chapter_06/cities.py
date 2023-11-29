# 6-11 Cities
cities = {
    'new york': {
        'country': 'united states',
        'population': '8,804,190',
        'fact': '''The Empire State Building is struck by lighting at least 
        23 times a year.''',
    },

    'berlin': {
        'country': 'germany',
        'population': '3,850,809',
        'fact': 'Berlin has more museums than rainy days.',
    },

    'moscow': {
        'country': 'russia',
        'population': '13,010,112',
        'fact': '''Moscow is home to the 200-tonne Tsar Bell, the largest bell 
        in the world.''',
    },
}

for key, value in cities.items():
    print(f"\nCity: {key.title()}")
    print(f"Country: {value['country'].title()}")
    print(f"Fact: {value['fact']}")