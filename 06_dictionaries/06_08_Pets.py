#create individual dictionaries
pet1 = {
    'name':'Gizmo',
    'owner':'Alyssa',
    'animal':'guinea pig'}


pet2 = {
    'name':'Captain Sparkles',
    'owner':'Keegan',
    'animal':'Cat'}


pet3 = {
    'name':'Lily',
    'owner':'Ava O',
    'animal':'Cat'}

pet4 = {
    'name':'Dunkin',
    'owner':'Ava S',
    'animal':'dog'}

#save them all in one dictionary
pets = [pet1,pet2,pet3,pet4]

for pet in pets:
    print(f"\n {pet}")