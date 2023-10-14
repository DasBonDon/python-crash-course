# 8-14 Cars
def make_car(manufacturer, model, **car_info):
    # Build a dictionary from the car info
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model
    return car_info

# Build the car and print it
car = make_car('volkswagen', 'beetle', year = '1965', color = 'yellow')
print(car)