# Weather Dashboard

This project fetches weather information from the OpenWeatherMap API and stores it in a local SQLite database (`weather.db`). You can query the last entries for any city and display them.

## Setup

1. Clone this repository.
2. Install dependencies:
- pip install -r requirements.txt

3. Add your OpenWeatherMap API key in `api.py`:
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

Notes: db.py 
- You **db.py** is your SQLite database file.
- You don’t need to create it manually
- This will be created automatically when you first run the program.
- Just make sure it’s in the same folder as main.py.


## USAGE: 
1. Run the program: python main.py

2. Enter a city name when prompted. The program will:
- Fetch the weather from the API
- Save it in **weather.db** 
- Show the last saved entries for that city

## Optional Helpers
**utils.py** contains functions to format and display weather data nicely.
