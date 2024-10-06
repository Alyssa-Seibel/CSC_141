#hold fav numbers for each person

fav_numbers = {
    'alyssa':['6','20'],
    'jordan':['13','6'],
    'keegan':['47','64'],
    'kayla':['59','11'],
    'kana':['2','99'],
              }
#print each person's name and their fav numbers
for name, numbers in fav_numbers.items():
    print(f"\n {name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" --> {number}")
