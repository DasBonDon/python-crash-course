# Module for 9-10
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