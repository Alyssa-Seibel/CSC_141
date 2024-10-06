#list 5 terms from python
glossary = {'string':'a sequence of characters enclosed in quotes',
            'list':'a build-in data type that allows you to store an ordered collection',
            'for loop':'a loop that iterates through code in its body for a set amount of times until a condition is met',
            'dictionary':'mutable data structures that allow you to store key-value pairs',
            'boolean':'true or false values'}
for gloss in glossary:
    print(f"{gloss}:\n\n {glossary[gloss]}\n\n\n")