import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=8064cd1cd8a24596b87113943242108&q='+city+'&aqi=no'

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in ", city, "is", description, 'and', temp, 'degrees.' )