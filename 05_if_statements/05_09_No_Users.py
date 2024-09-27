#Add an if test to hello_admin to make sure the list isnt empty


users = ['admin','doglover06','pizzaenjoyer2','rabbidanimal23','panda53']

for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
if not users:
    print('There are no users')
    

#when all users are removed, code prints there are no users.