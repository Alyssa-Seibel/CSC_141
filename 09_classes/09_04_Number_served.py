# create a class
class Restaurant:
    '''restaurant attributes'''
    
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.served = 0

    def describe_restuarant(self):
        print(f"\nYour restaurant name is {self.name}.")
        print(f"\nThe most popular food you serve is {self.food}.")


    def open_restaurant(self):
        print(f"\n{self.name} is now open!")

    def number_served(self):
        '''print a statement shower the number of people served'''
        print(f"\nThe restaurant has served {self.served} people.")

    def set_number_served(self, people):
        '''set number of people'''
        self.served = people

    def increment_number(self,people):
        '''add to the amount of people'''
        self.served += people

my_restaurant = Restaurant('Tropical Eats','Crab Cakes')
my_restaurant.set_number_served(45)
my_restaurant.increment_number(10)
print(f"\nMy restaurants name is {my_restaurant.name}")
print(f"\nThe most popular food there is {my_restaurant.food}")
my_restaurant.describe_restuarant()
my_restaurant.open_restaurant()
my_restaurant.number_served()