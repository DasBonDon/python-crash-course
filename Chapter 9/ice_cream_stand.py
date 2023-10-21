# 9-6 Ice Cream Stand
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
        self.flavors = []

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"They serve {self.type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, name, type='Dessert'):
        super().__init__(name, type)
        self.flavors = []

    def display_flavors(self):
        print(f"\nHere are our current flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

stand = IceCreamStand("Kevin's Ice Cream Stand")
stand.flavors = ['chocolate', 'vanilla', 'strawberry', 'rocky road']

stand.describe_restaurant()
stand.display_flavors()