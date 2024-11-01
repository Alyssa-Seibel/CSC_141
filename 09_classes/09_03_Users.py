# create a class for users
class User:
    def __init__(self, first_name, last_name, age, gender, fav_color):
        self.full_name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.fav_color = fav_color
     
    

    def describe_user(self):
        print(f"\nFull Name: {self.full_name}")
        print(f"\nAge: {self.age}")
        print(f"\nGender: {self.gender}")
        print(f"\nFav Color: {self.fav_color}")


    def greet_user(self):
        print(f"\nHello {self.full_name}")


user = User('Alyssa','Seibel','18','Female','Green')


user.describe_user()
user.greet_user()
