#Make a dictionary containing three major rivers and the country each river runs through.

dictionary = {'Mississippi':'North America',
              'Congo':'Africa',
              'Lena':'Asia'}
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

for river, country in dictionary.items():
    print (f"\n{river.title()} runs through {country.title()}.")

    #Use a loop to print the name of each river included in the dictionary

for river in dictionary.keys():
    print (f"\n{river.title()}")

#Use a loop to print the name of each country included in the dictionary.

for country in dictionary.values():
    print (f"\n{country.title()}")