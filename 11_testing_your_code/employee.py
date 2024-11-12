#8/10

class Employee():
    '''employee class'''
    def __init__(self,first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def get_raise(self, amount=5000):
        '''raise'''
        self.salary += amount