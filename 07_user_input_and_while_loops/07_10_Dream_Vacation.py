polling_active = True
responses = {}
while polling_active:
    name = input("What is your name?")
    response = input("What is your dream vacation?")

    responses[name] = response

    repeat = input("Would you like to take the poll again? (yes/no)")
    if repeat.lower() == 'no':
        polling_active = False

print("\n----Polling Results----")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")
    