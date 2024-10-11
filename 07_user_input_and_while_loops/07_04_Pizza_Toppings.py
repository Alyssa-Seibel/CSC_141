#a loop to enter pizza toppings

toppings = "\n Which pizza toppings would you like on your pizza? :"
toppings += "\n Enter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(toppings)
    print(f"A pizza with {message}")

