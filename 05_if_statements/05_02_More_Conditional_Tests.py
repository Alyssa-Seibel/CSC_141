#Tests for equality and inequality with strings

time = 5
print(time == 8)
print(time == 5)

#Tests using the lower() method

friends = ['Ava','Jordan','Arnia']
for friend in friends:
    if friend == 'Jordan':
        print(friend.lower())
    else:
        print(friend.upper())
print(friends)

''' Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to'''
print("\n\n\n\n")
age = 18
print("age = 18")

print("\nage < 12")
print(age < 12)
print("age > 12")
print(age > 12)
print("age >= 16")
print(age >= 16)
print("age <= 20")
print(age <= 20)

#Tests using the and keyword and the or keyword

name0 = 'jordan'
name1 = 'alyssa'

print( "\n\n\nare name0 == 'jordan' and name1 == 'kana'")
print(name0 == 'jordan' and name1 == 'kana')
print("\nare name0 == 'jordan' or name1 == 'kana'")
print(name0 == 'jordan' or name1 == 'kana')

#Test whether an item is in a list


print("\n\n\n")
sendoff = ['goodbye','bye','tschuss','auf wiedersehen']
print(sendoff)
print("\nis tschuss an option?")
print('tschuss' in sendoff)

#Test whether an item is not in a list

print("\n\n\n")
sendoff = ['goodbye','bye','tschuss','auf wiedersehen']
print(sendoff)

print('\n is adios an option?')
print('adios' in sendoff)






