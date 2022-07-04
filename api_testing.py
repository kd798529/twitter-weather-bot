import requests

from pprint import pprint

city = 'Kumasi'

country = 'Ghana'

API_KEY = 'fcddbb7286526afb642a9838fcfe6a8d'

weather_api = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s&units=imperial" %(city, country, API_KEY)

res = requests.get(weather_api)

weather_data = res.json()

# print(weather_data)

city = weather_data['name']
country = weather_data['sys']['country']
temp = str(weather_data['main']['temp'])
humidity = str(weather_data['main']['humidity'])
conditions =  weather_data['weather'][0]['description']


pprint(weather_data)
#print('City: %s\nTemp: %s\n ' %(city, humidity))

