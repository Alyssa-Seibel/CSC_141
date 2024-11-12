#1/10
#make a calculator

print("Give me two numbers and i'll add them together!")
print("Type 'q' to quit.")

try:
    first = input("\nFirst number: ")
   
    second = input("Second number: ")
    
    answer = int(first) + int(second)
        
except ValueError:
    print("\nYou cannot divide letters!")
else:
    
    print(f"\n{answer}")
   

