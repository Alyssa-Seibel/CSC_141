dinner = ['Keegan','Lex','Mirror']


print (f"\n\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n\n {dinner[2].title()}, will you come to dinner with me?')

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

#print(dinner[8])

print(dinner[4])