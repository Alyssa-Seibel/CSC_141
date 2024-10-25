def make_shirt(message, size='Large'):
    print(f"\nYou ordered a {size.title()} shirt.")
    print(f'\nThe message on your shirt is "{message.title()}"')

make_shirt(message ='I Love Python')

def make_shirt2(size, message='I Hate Python'):
    print(f"\nYou ordered a {size.title()} shirt.")
    print(f'\nThe message on your shirt is "{message.title()}"')

make_shirt2(size = 'Large')
make_shirt2(size='medium')