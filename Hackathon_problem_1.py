# __Author__ = "Pranav Chandran"
# __Date__ = 27-05-2023
# __Time__ = 14:43
# __FileName__ = Hackathon_problem_1.py
"""
Problem Statement

Python - Weather Forecasting Tool

Create a command-line tool that accepts a city's name and returns the current
weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse
it using Python. Your solution should demonstrate how GitHub Copilot can help you
with API usage, data parsing, and error handling.
"""
import requests
import json
import os
from dotenv import load_dotenv

# Define the API endpoint and API key
url = 'https://api.openweathermap.org/data/2.5/weather'
load_dotenv()
api_key = os.getenv('API_KEY')


# Define a function to get the weather data for a city
def get_weather(city: str) -> None:
    # Make a request to the API with the city name and API key
    response = requests.get(url, params={'q': city, 'appid': api_key})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = json.loads(response.text)

        # Extract the relevant weather information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        # Print the weather information
        print(f'Weather in {city}: {weather}')
        print(f'Temperature: {temperature} K')
        print(f'Humidity: {humidity}%')
    else:
        # Print an error message if the request was unsuccessful
        print(f'Error getting weather data for {city}')


# Get the city name from the user
city = input('Enter a city name: ')

# Get the weather data for the city
get_weather(city)
