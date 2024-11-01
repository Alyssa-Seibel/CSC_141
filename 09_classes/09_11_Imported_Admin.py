from user_privileges_admin import Admin, User

keegan = Admin('Keegan','Fails','18','Male','Red')
keegan.describe_user()
keegan_privileges = [
    'Can post','Can remove posts','Can ban']
keegan.privileges.privileges = keegan_privileges


keegan.privileges.show_privileges()


