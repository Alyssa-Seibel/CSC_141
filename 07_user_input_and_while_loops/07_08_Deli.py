#make a list of sandwich orders
sandwich_orders = ['Tuna','Ham and Cheese','Turkey and Cheese','Italian']

#Make and empty list
finished_sandwiches = []

#make each sandwich in the list
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Making:\n\t {current_order.title()} sandwich")
    finished_sandwiches.append(current_order)

#display finish products
print("\n The following orders are ready for pickup:")
for finished in finished_sandwiches:
    print(f"\n{finished} sandwich.")