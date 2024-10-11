#input 

question = input("How many people are in your dining group?")

question = int(question)

if question > 8:
    print("You will have to wait for a table...")
else:
    print("Your table is ready...")