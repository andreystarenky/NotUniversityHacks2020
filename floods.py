import json
import requests

# DATA FOR WEATHER IN GIVEN LOCATION
weatherData = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&%20exclude=hourly,daily&appid=83231dc5b0b225eb97bb206cc1023ece")

# GET WATER DATA FOR GIVEN STATION
waterData = requests.get("https://vps267042.vps.ovh.ca/scrapi/stations?page=7&key=-M99M-mwrZtTa9QBKKgx")


with open("weather.json", 'r', ) as file:
    weatherString = file.read()

with open("water.json", 'r', ) as file:
    waterString= file.read()


weatherData = json.loads(weatherData.text)
waterData = json.loads(waterData.text)

# DEBUG
print("DAILY PREDICTIONS FOR MODEL SET: " + str(weatherData["daily"]))
print(waterData["message"]["history"][0]["value"])
print(waterData["message"]["history"][(len(waterData["message"]["history"])-1)]["value"])

# LOAD TF Model with Data and first and final values to generate resultant prediction
#tf_model.MyModel.setVals(waterData["message"]["history"][0]["value"],
 #                        waterData["message"]["history"][(len(waterData["message"]["history"])-1)]["value"],
  #                       weatherData["daily"] + waterData)