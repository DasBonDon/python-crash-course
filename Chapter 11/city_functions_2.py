# Module for 11-2
def get_city_country(city, country, population=''):
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()