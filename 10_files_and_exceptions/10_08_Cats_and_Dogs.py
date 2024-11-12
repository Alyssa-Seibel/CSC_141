# 2/10
# reading files
files = ['cats.txt','dogs.txt']

for file in files:
    print(f"\nReading file: {file}")
    try:
        with open(file) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Sorry, the file {file} is not found.")
        
        


