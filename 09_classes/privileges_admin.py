from user import User

class Admin(User):
    '''Make different attribues for admin'''
    def __init__(self,first_name, last_name, age, gender, fav_color, privileges=[None]):
        super().__init__(first_name, last_name, age, gender, fav_color)
        self.privileges = Privileges()

class Privileges:
    '''have only privilege attribute'''
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
    
        if self.privileges:
            print(f'This person has these privileges:\n{self.privileges}')
        else:
            print('This user has no privileges')

