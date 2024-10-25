def city_country(city, country):
    return(city.title() + "," + country.title())

city = city_country('chicago','USA')
print(city)

city = city_country('Reading','USA')
print(city)

city = city_country('Wildwood','USA')
print(city)