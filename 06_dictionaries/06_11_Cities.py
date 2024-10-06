cities ={
    'New York' : {
        'country':'USA',
        'population': '8.336 mill',
        'fact':'The first pizzeria in USA was in New York'
    },
    'Chicago': {
        'country':'USA',
        'population': '2.665 mill',
        'fact':'Home of the first ferris wheel'
    },
    'Philadelphia': {
        'country':'USA',
        'population': '1.567 mill',
        'fact':'birthplace of the Declaration of Independence'
    },
}
for city, info in cities.items():
    print(f"\n{city}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")