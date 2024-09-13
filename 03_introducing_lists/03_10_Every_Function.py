colors = ['green' , 'pink' , 'purple' , 'blue' , 'yellow' , 'red']
print(colors)

print(colors[2])

message = f"my favorite color is {colors[0].title()}"
print(message)

colors[1] = 'hot pink'
print(colors)

colors.append('brown')
print(colors)

colors.insert(0, 'black')
print(colors)

del colors[0]
print(colors)

popped = colors.pop()
print(colors)
print(popped)

first_fav = colors.pop(2)
print(f"my first favorite color was {first_fav.title()}")

colors.remove('hot pink')
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

print(sorted(colors))
print(colors)

colors.reverse()
print(colors)

print(len(colors))

