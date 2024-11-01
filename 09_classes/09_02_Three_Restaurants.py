# create a class
class Restaurant:
    '''restaurant attributes'''
    
    def __init__(self, name, food, age, tables, chefs):
        self.name = name
        self.food = food
        self.age = age
        self.tables = tables
        self.chefs = chefs

    def describe_restuarant(self):
        print(f"\nYour restaurant name is {self.name}.")
        print(f"\nThe most popular food you serve is {self.food}.") 
        print(f"\nThe amount of tables in {self.name} are {self.tables}.")
        print(f"\n{self.name} is {self.age} years old!")
        print(f"\nThe amount of chefs working there are {self.chefs}.")

    def open_restaurant(self):
        print(f"\n{self.name} is now open!")


my_restaurant = Restaurant('Tropical Eats','Crab Cakes','4','40','6')

my_restaurant.describe_restuarant()
my_restaurant.open_restaurant()