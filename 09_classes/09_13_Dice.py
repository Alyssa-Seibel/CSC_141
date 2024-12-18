'''This makes randomizing an option'''
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint (1, self.sides)
    

#make a 6 side die

d6 = Die()

results=[]
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-sides-die:")
print(results)    


# make a 10-sided-die
d10 = Die(sides=10)

results=[]
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print("10 rolls of a 10-sided-die:")
print(results)


# make a 20-sided-die
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print("10 rolls of a 20-sided-die:")
print(results)