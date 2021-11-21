#! python3
# weather.py - A program to output weather info of any location from command line.

import json, sys, requests

APPID = '#######################'

if len(sys.argv) < 2:
    print('Usage: weather.py city_name, state code, country code')
    sys.exit()

location = ''.join(sys.argv[1:])

#TODO: Download the JSON data from OpenWeatherMap.org's API.

url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' %(location, APPID)

response = requests.get(url)
response.raise_for_status

#Uncomment to Print JSON Data
#print(response.text)

#TODO: Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.

w = weatherData['list']
print('Current weather in %s:' %location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], '-Temp.', w[0]['main']['temp']-273)}
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])#, '-Temp.', w[1]['temp'][1]['main']-273)
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])#, '-Temp.', w[1]['temp'][1]['main']-273)
