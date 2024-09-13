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
