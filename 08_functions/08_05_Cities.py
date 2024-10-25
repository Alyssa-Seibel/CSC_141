def describe_city(name, country='USA'):
    print(f'\n{name.title()} is in {country.title()}.')

# name 2 in the country and 1 not in the default country
describe_city(name='chicago')
describe_city(name='Reading')
describe_city(name='Hamburg')