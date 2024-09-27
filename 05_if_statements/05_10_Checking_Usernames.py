# Make a list of five or more usernames called current_users

current_users = ['girlygirl33','doglover06','pizzaenjoyer2','rabbidanimal23','panda53']

#Make another list of five usernames called new_users. Make sure one or two repeat from current.
new_users = ['emilyh3','lily339','DOGlover06','jonnylaw','girlyGirl33']

#Convert current to lowercase for case-insesitive 
lower_current_users = [user.lower() for user in current_users]

'''Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.'''

#make sure to compare each in lowercase
for new in new_users:
    if new.lower() in lower_current_users:
        print(f"{new} is unavailable. Please pick a different username")
    else:
        print(f"{new} is available. Please continue.")