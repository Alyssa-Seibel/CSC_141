
#add pastrami 3 times
sandwich_orders = ['Pastrami','Tuna','Ham and Cheese','Pastrami','Turkey and Cheese','Pastrami','Italian']
finished_orders = []
print("---Sandwich Orders---")
print(f"\n Sorry if you ordered Pastrami. We are out.")
while 'Pastrami'in sandwich_orders:
   sandwich_orders.remove('Pastrami') 
while sandwich_orders:
    current_order = sandwich_orders.pop()
   
    print(f"\nMaking a:\n\n\t {current_order} sandwich...")
    finished_orders.append(current_order)

print(f"\nThe orders ready for pickup are:")
for finished in finished_orders:
    print(finished)
    
    
