#2/10
#make a calculator

print("Give me two numbers and i'll add them together!")
print("Type 'q' to quit.")

while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break

    second = input("Second number: ")
    if second == 'q':
        break
    
    try:
        answer = int(first) + int(second)
        
    except ValueError:
        print("\nYou cannot divide letters!")
    else:
        print(f"\n{answer}")
   
