#Make a list of five or more usernames, including the name 'admin'

users = ['admin','doglover06','pizzaenjoyer2','rabbidanimal23','panda53']

#if user is admin print special message. All others get a generic greeting.

for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")