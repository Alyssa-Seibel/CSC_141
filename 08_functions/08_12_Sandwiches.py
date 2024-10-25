def sandwich_order(*toppings):
    print('\nWhat toppings do you want on your sandwich?')
    for top in toppings:
        print(f'- {top}')

order = sandwich_order('lettuce','tomato','cheese')
order = sandwich_order('cheese')
order = sandwich_order('salami','ham','cheese')