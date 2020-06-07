# H2Flow
NotUniversity Hacks 2020 Submission

## About
H2Flow is a Flask Web App that uses Machine Learning in order to predict floods and droughts from historical water and weather data.

Data is fetched from the Canada Water Data API as well as the OpenWeather API. This data is then parsed into our Tensorflow model which will make predictions about future floods and droughts with water levels in the next 7 days. It will then send all of the data, the model, and the predictions to the web app which will display the values on the website.
