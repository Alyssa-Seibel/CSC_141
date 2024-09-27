#storing 1-9 in a list
numbers = [1,2,3,4,5,6,7,8,9]


#loop through list
#for number in numbers:
#    print(number)

#adding correct ordinal

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")