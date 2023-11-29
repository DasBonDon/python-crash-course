# 11-2 Population
from city_functions_2 import get_city_country

def test_city_country():
    formatted_name = get_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    formatted_name = get_city_country('santiago', 'chile', '5,000,000')
    assert formatted_name == 'Santiago, Chile - Population 5,000,000'