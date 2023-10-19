# 9-2 Three Restaurants
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"They serve {self.type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")

restaurant = Restaurant("Kevin's Pizza", 'Italian')
restaurant.describe_restaurant()

restaurant = Restaurant('City Wok', 'Chinese')
restaurant.describe_restaurant()

restaurant = Restaurant('Chipotle', 'Mexican')
restaurant.describe_restaurant()