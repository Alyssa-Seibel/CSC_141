#Make a list of your favorite fruits
fav_fruits = ['strawberries','bananas','tomatoes','cherries']

'''Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!'''

#If you want everything to print then start with line 11.
#if you dont, then get rid of line 11 and change the statements to: if 'strawberries' in fav_fruits

for fruit in fav_fruits:
    if fruit == 'strawberries':
        print("Sometimes I like strawberries")
    elif fruit == 'bananas':
        print ("Bananas are good for breakfast")
    elif fruit == 'tomatoes':
        print("I love tomatoes")
    elif fruit == 'cherries':
        print("I like to eat fresh cherries")
    else:
        print("That is not my favorite")
