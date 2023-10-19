# 9-4 Number Served
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"They serve {self.type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("Kevin's Pizza", 'Italian')
print(restaurant.number_served)

restaurant.number_served = 25
print(restaurant.number_served)

restaurant.set_number_served(60)
print(restaurant.number_served)

restaurant.increment_number_served(100)
print(restaurant.number_served)