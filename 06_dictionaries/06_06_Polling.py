



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python'}

#Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
names = ['Jordan','Keegan','Kana','jen','edward']

#Loop through the list of people who should take the poll. 

for name in names:

    if name.lower() in favorite_languages:
        print(f"\nThank you {name.lower()} for taking the poll!")
    else:
        print(f"\nHello {name.title()}, please take the poll!")
