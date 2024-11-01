# write a new class called admin that inherits from user
# create a class for users
class User:
    def __init__(self, first_name, last_name, age, gender, fav_color):
        self.full_name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.fav_color = fav_color
        self.login_attempts = 0
    

    def describe_user(self):
        print(f"\nFull Name: {self.full_name}")
        print(f"\nAge: {self.age}")
        print(f"\nGender: {self.gender}")
        print(f"\nFav Color: {self.fav_color}")


    def greet_user(self):
        print(f"\nHello {self.full_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
'''       
user = User('Alyssa','Seibel','18','Female','Green')

user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
'''

class Admin(User):
    '''Make different attribues for admin'''
    def __init__(self,first_name, last_name, age, gender, fav_color, *privileges):
        super().__init__(first_name, last_name, age, gender, fav_color)
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nThis user has these privileges:\n  {self.privileges}.")

admin = Admin('Alyssa','Seibel','18','Female','Green','Can post','Can remove posts','Can ban')
admin.describe_user()
admin.greet_user()
admin.show_privileges()