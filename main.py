# rest apis 
# Application Program Interface
# destination in the internet where you can get data from 

import requests # request something from the internet
import json # JSON is Javascript Object Notation

response = requests.get("https://randomuser.me/api/")
# print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
first = response.json()['results'][0]['name']['first']
last = response.json()['results'][0]['name']['last']
print(first)
print(last)
email = response.json()['results'][0]['email']
print(email)
number = response.json()['results'][0]['phone']
print(number)
city = response.json()['results'][0]['location']['city']
print(city)
postalCode = response.json()['results'][0]['location']['postcode']
print(postalCode)
address = response.json()['results'][0]['location']['street']
print(address)
birthday = response.json()['results'][0]['dob']
print(birthday)
userID = response.json()['results'][0]['login']['uuid']
print(userID)
regage = response.json()['results'][0]['registered']['age']
print(regage)