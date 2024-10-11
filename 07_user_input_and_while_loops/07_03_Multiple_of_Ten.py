#ask for a number

number = input("Pick a number and ill tell you if it is a multiple of ten-->")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of ten!")
else:
    print(f"\n{number} is not a multiple of ten.")
    