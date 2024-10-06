
people = {
    'Jordan': {
    'first': 'Jordan',
    'last' : 'Dix',
    'age' : '18',
    'location' : 'Marlton, NJ',
    },
    'Keegan':{
    'first':'Keegan',
    'last':'Fails',
    'age':'18',
    'location':'Delco, PA',
    },
    'Alyssa':{
    'first':'Alyssa',
    'last':'Seibel',
    'age':'18',
    'location':'Horsham, PA',
    }
}

#loop through all info

for name, info in people.items():
    print(f"Details for {name}:")
    for key, value in info.items():
        print(f" {key.title()}: {value}")
    print(f"\n\n")