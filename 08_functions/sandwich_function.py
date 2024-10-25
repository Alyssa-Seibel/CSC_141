def sandwich_order(*toppings):
    print('\nWhat toppings do you want on your sandwich?')
    for top in toppings:
        print(f'- {top}')