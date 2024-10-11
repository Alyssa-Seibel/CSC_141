toppings = "\n Which pizza toppings would you like on your pizza? :"
toppings += "\n Enter 'quit' to end the program."

message = ""#conditional test
while message != 'quit':
    message = input(toppings)
    if message != 'quit':
        print(f"A pizza with {message}")

active = True
while active:#active variable
    message = input(toppings)
    if message.lower() == 'quit':
        active = False
    else:
        print(f"A pissa with {message}")

while True:#break statement
    message = input(toppings)
    if message.lower() == 'quit':
        break   
    print(f"A pizza with {message}")



