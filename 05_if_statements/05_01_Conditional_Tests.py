''' Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
'''

# first create a variable

picnic_food = ['sandwich','melon','juice','water','cheese','soup']
guests = ['mouse','cow','cat','dog','rabbit']

#print a statement checking if something is true or false
#to check in a list you must use '' in variable
#to check just a variable use variable == blank
print("Are we bringing pie to the picnic?")
print('pie' in picnic_food)

print("Well that sucks. What about cheese?")
print('cheese'in picnic_food)

print("Well we obviously need crackers with the cheese right?")
print('crackers' in picnic_food)

print("Well that sucks. Do we have plates on the list?")
print ('plates' in picnic_food)

print("What drinks do we have? water? milk?")
print('water' in picnic_food)
print('milk' in picnic_food)

print("Well lets check the guest list")

print("Is sheep and rabbit coming?")
print('sheep' in guests)
print('rabbit' in guests)

print("How about cat and dog?")
print('cat' in guests)
print('dog' in guests)

print("does guests == mouse?")
print('mouse' in guests)