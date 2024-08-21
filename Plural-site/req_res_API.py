import requests

respense = requests.get('http://api.open-notify.org/astros.json')
json = respense.json()

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])