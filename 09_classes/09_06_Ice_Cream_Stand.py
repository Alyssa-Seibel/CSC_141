# creating a child class off of restaurant
# create a class
class Restaurant:
    '''restaurant attributes'''
    
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.served = 0

    def describe_restaurant(self):
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
'''
my_restaurant = Restaurant('Tropical Eats','Crab Cakes')
my_restaurant.set_number_served(45)
my_restaurant.increment_number(10)
print(f"\nMy restaurants name is {my_restaurant.name}")
print(f"\nThe most popular food there is {my_restaurant.food}")
my_restaurant.describe_restuarant()
my_restaurant.open_restaurant()
my_restaurant.number_served()
'''



# ice cream stand class
class IceCreamStand(Restaurant):
    '''aspects of a restaurant with ice cream shop attributes'''

    def __init__(self, name, food, *flavors):
        '''grab parent class attributes'''
        self.flavors = flavors
        super().__init__(name,food)

    def icecream_flavors(self):
        print(f"\n{self.name} has these flavors of ice cream:\n  {self.flavors}.")


my_icecream_shop = IceCreamStand('Cold Stone','Ice Cream','Chocolate','Vanilla','Strawberry')
my_icecream_shop.set_number_served(14)
my_icecream_shop.describe_restaurant()
my_icecream_shop.open_restaurant()
my_icecream_shop.number_served()
my_icecream_shop.icecream_flavors()