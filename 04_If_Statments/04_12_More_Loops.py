pizzas = ['pepper and onion','white','margherita']
friend_pizza = pizzas[:]
pizzas.append('pepperoni')
friend_pizza.append('cheese')

for pizza in pizzas:
    print(f'I love {pizza} pizza')
print("\n")
for friend in friend_pizza:
    print(f'My friend loves {friend} pizza')