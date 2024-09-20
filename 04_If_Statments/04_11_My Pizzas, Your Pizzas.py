pizzas = ['pepper and onion','white','margherita']
friend_pizza = pizzas[:]

for pizza in pizzas:
    print(f'Do you like {pizza.title()} pizza?\n')

print("Of course I like pizza")

pizzas.append('pepperoni')
friend_pizza.append('cheese')

print("\nmy favorite pizzas are...")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are...")
for friend in friend_pizza:
    print(friend)