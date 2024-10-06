#adding info
people = {
    'Jordan': {
    'first': 'Jordan',
    'last' : 'Dix',
    'age' : '18',
    'location' : 'Marlton, NJ',
    'gender':'girl',
    },
    'Keegan':{
    'first':'Keegan',
    'last':'Fails',
    'age':'18',
    'location':'Delco, PA',
    'gender':'boy',
    },
    'Alyssa':{
    'first':'Alyssa',
    'last':'Seibel',
    'age':'18',
    'location':'Horsham, PA',
    'gender':'girl',
    }
}

#loop through all info
#adding spacers
for name, info in people.items():
    print(f"Details for {name}:")
    print("-------------------------")
    for key, value in info.items():
        print(f"{key.title()}:\n--> {value}")
    print(f"\n\n")