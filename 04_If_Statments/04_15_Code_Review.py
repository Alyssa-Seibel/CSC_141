'''Choose three of the programs I've written in this chapter and modify each
one to comply with PEP 8
1. Use four spaces for each indentation level
2. Use less than 80 characters on each line
3. Don’t use blank lines excessively in your program files'''


pizzas = ['pepper and onion','white','margherita']

#instead of hitting tab, do 4 spaces
for pizza in pizzas:
    print(f'Do you like {pizza.title()} pizza?\n')

print("Of course I like pizza")

#no excessive spaces
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

pizzas = ['pepper and onion','white','margherita']
friend_pizza = pizzas[:]
pizzas.append('pepperoni')
friend_pizza.append('cheese')

#Used 4 spaces instead of tab
for pizza in pizzas:
    print(f'I love {pizza} pizza')
print("\n")
for friend in friend_pizza:
    print(f'My friend loves {friend} pizza')