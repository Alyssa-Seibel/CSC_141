#8/10

from city_functions import city_country

def test_city_country():
    '''testing if they work'''
    format = city_country('Reading','Pennsylvania')
    assert format == 'Reading, Pennsylvania'