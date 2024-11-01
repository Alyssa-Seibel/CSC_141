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