# 10/10
# collect all names and put into a different path

guest_book = open ('guest_book.txt','w')
while True:
    name = input("Pleae enter your name: ")
    if name == 'quit':
        break
   
    guest_book.write(name + '\n')
   





    
    