import tweepy
import time
import requests
import re
import requests

# prints the given string in the console
print('This is my twitter bot')


# tweepy config

CONSUMER_KEY = 'eHNqMF8DyaGYN4KTgREEBebaB'
CONSUMER_SECRET = 'ER3qupooKJejzZZEu1ZqVguvsHle0r0rQrlz2Maaypp1V35nKX'
ACCESS_KEY = '1062539306672287749-sSq5wvm8xNFFzUuG3Q1M02235HCdUW'
ACCESS_SECRET = 'aGJvDmHEOLEM7fmzevKAEF2WYtlrbLqjN67sn9hfCGUOj'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# storing and retrieving the last seen id from the tweet

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# parsing the JSON file into a python dictionary

import json
with open('cities.json') as json_file:
    CITIES_COUNTRIES = json.load(json_file)


#function that searches the list of cities to see if it exists
def simpleSearch(arr, location):
  
  found = False
  for city in arr:
    if city['city'].lower() == location.lower():
      found = True
  return found

#function that grabs the country
def simpleCountrySearch(arr, location):
  
  found = ''
  for city in arr:
    if city['city'].lower() == location.lower():
      found = city['country']
  return found




# Function that sorts the data

def grabCity(elem):
  return elem["city"]

def sort_alpha_by_city(arr):
  return arr.sort(key=grabCity)

sort_alpha_by_city(CITIES_COUNTRIES)

# The function that replies to tweets

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        since_id= last_seen_id,
        #tweet_mode='extended'
    )

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        
        # grabs the name of the city from the tweet
        result1 = re.findall('\s.+', str(mention.text))
        city_name = result1[0][1:]



        if simpleSearch(CITIES_COUNTRIES, city_name) == True:
            print('found weather app tweet mention!', flush=True)
            print('responding back ...', flush=True)
            print(city_name)

            # open weather api config
            city = city_name

            country = simpleCountrySearch(CITIES_COUNTRIES, city_name)

            API_KEY = '37ae7082326f852682b047bfc4381ace'

            weather_api = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s&units=imperial" %(city, country, API_KEY)

            res = requests.get(weather_api)

            weather_data = res.json()

            user_city = weather_data['name']
            user_country = weather_data['sys']['country']
            temp = str(weather_data['main']['temp'])
            humidity = str(weather_data['main']['humidity'])
            conditions =  weather_data['weather'][0]['description']

            api.update_status(status='@' + mention.user.screen_name + ' ' + 'Location: '+ user_city +', ' + user_country + '\n' + 'Temp: ' + temp + 'F' +'\n' + 'Humidity: ' + humidity + '%' + '\n' + 'Conditions: ' + conditions , in_reply_to_status_id =mention.id)
        else:
            api.update_status(status='@'+ mention.user.screen_name + ' Sorry I could not find your city. Please mention me with just a city. Thank you!', in_reply_to_status_id =mention.id )

while True:
    reply_to_tweets()
    time.sleep(15)