contacts = {
    'number' : 4,
    'students':
    [
        {'name' : 'Madhu', 'email': 'mad.xyz@gmail.com'},
        {'name' : 'Mishti', 'email': 'mis.xyz@gmail.com'},
        {'name' : 'Pari', 'email': 'par.xyz@gmail.com'},
        {'name' : 'Priya', 'email': 'pri.xyz@gmail.com'}
    ]
}

print('Students emails:')
for student in contacts['students']:
    print(student)