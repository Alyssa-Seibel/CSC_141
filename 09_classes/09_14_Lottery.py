from random import choice
rand = [1,2,3,4,5,6,7,8,9,10,'a','t','k','j','m']

def roll():
    return choice in range(0,14)

for roll_num in range(4):
    results = choice(rand)
    print(results)

if results == ['6','a','3','m']:
    print("You won the lottery!")
else:
    print("You didn't win. Try again next time.")