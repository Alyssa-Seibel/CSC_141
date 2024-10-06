# replace your series of print() calls with a loop that runs through the dictionary’s keys and values. 

#list 5 terms from python
glossary = {'string':'a sequence of characters enclosed in quotes',
            'list':'a build-in data type that allows you to store an ordered collection',
            'for loop':'a loop that iterates through code in its body for a set amount of times until a condition is met',
            'dictionary':'mutable data structures that allow you to store key-value pairs',
            'boolean':'true or false values',
            'tuple':'An ordered list of elements',
            'function':'A block of program statements which can be used repetitively',
            'list':'A data structure in Python that is a mutable, or changeable, ordered sequence of elemtnets',
            'float':'a number represented with decimal points',
            'variable':'A reserved memory location to store values'}


for term, definition in glossary.items():
    print(f"\n\n\nTerm: {term}")
    print(f"\nDefiniton: {definition}")