# 9-1 Restaurant
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

print(f"My restaurant is called {restaurant.name}.")
print(f"We serve {restaurant.type} cuisine!\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()