# 11-1 City, Country
from city_functions import get_city_country

def test_city_country():
    formatted_name = get_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'