dinner = ['Keegan','Lex','Mirror']


print (f"\n\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n\n {dinner[2].title()}, will you come to dinner with me?')

print(len(dinner))

print("\n------------------------")
print("Mirror cannot make it to dinner...")
print("------------------------")

dinner[2] = 'Kevin'

print (f"\n\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n\n {dinner[2].title()}, will you come to dinner with me?')


print("\n------------------------")
print("A larger table is available...")
print("------------------------")

dinner.append('Luca')
dinner.insert(2,'Kana')
dinner.insert(0,'Jordan')

print (f"\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n\n {dinner[2].title()}, will you come to dinner with me?')
print (f"\n\n {dinner[3].title()}, will you come to dinner with me?")
print (f"\n\n {dinner[4].title()}, will you come to dinner with me?")
print (f'\n\n {dinner[5].title()}, will you come to dinner with me?')


print("\n------------------------")
print("unfortunatly, your table is taken. Only two guests can attend...")
print("------------------------")

print("\nPlease pluck off your guests...")
print(*dinner)

sorry1 = dinner.pop()
print(f'\n "Sorry {sorry1}, you can\'t come."')

sorry2 = dinner.pop()
print(f'\n "Sorry {sorry2}, you aren\'t allowed to eat with us."')

sorry3 = dinner.pop()
print(f'\n"Sorry {sorry3}, you can\'t sit with us."')

sorry4 = dinner.pop()
print(f'\n"Sorry {sorry4}, bye."')

print(f'\n "Sorry but {sorry1}, {sorry2}, {sorry3}, and {sorry4} have to go"')
print(f'\n The people remaining are:')
print(*dinner)


print('\n*the rest of the guests left* "I guess no one wants to come anymore.."')
del dinner[0]
del dinner [0]
print(dinner)

