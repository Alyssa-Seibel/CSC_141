# create a class
class Restaurant:
    '''restaurant attributes'''
    
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def describe_restuarant(self):
        print(f"\nYour restaurant name is {self.name}.")
        print(f"\nThe most popular food you serve is {self.food}.")


    def open_restaurant(self):
        print(f"\n{self.name} is now open!")


my_restaurant = Restaurant('Tropical Eats','Crab Cakes')

print(f"\nMy restaurants name is {my_restaurant.name}")
print(f"\nThe most popular food there is {my_restaurant.food}")
my_restaurant.describe_restuarant()
my_restaurant.open_restaurant()