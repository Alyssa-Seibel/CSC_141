prompt = ("Please enter your age and i'll price your ticket")
prompt += (" (Enter 'exit' to exit):")

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        try:
            age = int(age)

            if age < 3:
                print ("Your ticket is free") 
            elif 3<= age <=  12:
                print("Your ticket is $10")
            elif age >= 13:
                print("Your ticket is $15") 
            else:
                print("Invalid age. Please enter a valid age.")
        except ValueError:
            print("Please enter a valid number for your age.")


