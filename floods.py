import json
import requests

# DATA FOR WEATHER IN GIVEN LOCATION
#weatherData = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&%20exclude=hourly,daily&appid=83231dc5b0b225eb97bb206cc1023ece")

# GET WATER DATA FOR GIVEN STATION
#waterData = requests.get("https://vps267042.vps.ovh.ca/scrapi/stations?page=7&key=-M99M-mwrZtTa9QBKKgx")
#weatherData = requests.get()

with open("weather.json", 'r', ) as file:
    weatherString = file.read()

#print(weatherString)

testData = json.loads(weatherString)

print(testData["daily"])