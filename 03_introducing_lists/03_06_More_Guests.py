dinner = ['keegan','lex','mirror']


print (f"\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n {dinner[2].title()}, will you come to dinner with me?')

print("------------------------")
print("Mirror cannot make it to dinner...")
print("------------------------")

dinner[2] = 'Kevin'

print (f"\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n {dinner[2].title()}, will you come to dinner with me?')

print("------------------------")
print("A larger table is available...")
print("------------------------")

dinner.append('Luca')
dinner.insert(2,'Kana')
dinner.insert(0,'Jordan')

print (f"\n {dinner[0].title()}, will you come to dinner with me?")
print (f"\n {dinner[1].title()}, will you come to dinner with me?")
print (f'\n {dinner[2].title()}, will you come to dinner with me?')
print (f"\n {dinner[3].title()}, will you come to dinner with me?")
print (f"\n {dinner[4].title()}, will you come to dinner with me?")
print (f'\n {dinner[5].title()}, will you come to dinner with me?')
