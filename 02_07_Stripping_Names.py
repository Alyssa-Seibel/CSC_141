
name = "    Alyssa Seibel   "
name_2 = "  keegan "
message = "Names"


#\t - tab
#\n - new line
#When using different variables at once, use an f-string

print(f"{message}\n\t{name}\n\t{name_2}")

#lstrip() strips the extra spaces on the left
print(f"{message}\n\t{name.lstrip()}\n\t{name_2.lstrip()}")

#rstrip() strips the space on the right
print(f"{message}\n\t{name.rstrip()}\n\t{name_2.rstrip()}")

#strip() strips the space on both sides
print(f"{message}\n\t{name.strip()}\n\t{name_2.strip()}")
