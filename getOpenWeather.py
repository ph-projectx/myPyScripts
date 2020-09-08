#!/usr/bin/python3
#getOpenWeather.py = Prints the weather for a location from command line


APPID = '125586a42d0bd62391a4b2c4b3c59057'

import json, requests, sys, pprint

#compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

#Download the JSON data from openWeatherMap.org API
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid='+ APPID
r = requests.get(url)

if r.status_code == 200:
    print('Success')
else:
    print('Failed')

data = r.text

#load json data into a python variable
weatherDATA = json.loads(data)

#printer weather description
city = weatherDATA['name']
country_code = weatherDATA['sys']['country']
weather_main = weatherDATA['weather'][0]['main']
weather_desc = weatherDATA['weather'][0]['description']

print(f"Current Weather in {city},{country_code}:")
print(f"{weather_main} - {weather_desc}")
