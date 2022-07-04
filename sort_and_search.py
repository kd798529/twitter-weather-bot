import json
with open('cities.json') as json_file:
    CITIES_COUNTRIES = json.load(json_file)

def grabCity(elem):
  return elem["city"]

def sort_alpha_by_city(arr):
  return arr.sort(key=grabCity)

sort_alpha_by_city(CITIES_COUNTRIES)

midpoint_index = int(0 + (len(CITIES_COUNTRIES) - 1)/2)
midpoint_city = CITIES_COUNTRIES[midpoint_index - 1]['city']
midpoint_place = { CITIES_COUNTRIES[midpoint_index]['city'], CITIES_COUNTRIES[midpoint_index]['country']}
# print(midpoint_place)

# Binary search

def BS(arr, l, r, target):
  if r >= l:
    mid = int(l + (r - 1)/2)
    if arr[mid]['city'].lower() == target.lower():
      return True
    elif arr[mid]['city'].lower() > target.lower():
      return BS(arr, l, mid - 1, target)
    else:
      return BS(arr, mid + 1, r, target)
  else:
   return False

result = BS(CITIES_COUNTRIES, 0, len(CITIES_COUNTRIES) - 1, 'Boston')
# print(result)
# mid point city == Lypcha 

# Simple search

def simpleSearch(arr, location):
  
  found = False
  for city in arr:
    if city['city'].lower() == location.lower():
      found = True
  return found

#print(simpleSearch(CITIES_COUNTRIES, 'kumasi'))

# Find country

def simpleCountrySearch(arr, location):
  
  found = ''
  for city in arr:
    if city['city'].lower() == location.lower():
      found = city['country']
  return found

import re

tweet = "@elsparkojr Oslo"

result1 = re.findall('\s.+', tweet)
city_name = result1[0][1:]

#print(city_name)


