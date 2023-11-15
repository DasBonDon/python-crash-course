# Class for 11-3
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = int(annual_salary)

    def give_raise(self, raise_amount=5000):
        self.annual_salary += raise_amount
        print(f"{self.first_name} {self.last_name}'s annual salary has been "
              f"increased by {raise_amount}! Their new annual salary is "
              f"{self.annual_salary}.")