menus = {
    'Breakfast' : ['Egg Sandwich', 'Begel', 'Coffee'],
    'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
    'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco']
}

for name, menu in menus.items():
    print(name, ':', menu)


######################### another example #########################

person = {
    'name' : 'Madhu Ojha',
    'city' : 'Solna',
    'age'  : '37'
}

print(person.get('name'), 'is', person.get('age'), 'years old, lives in', person.get('city'), '.')