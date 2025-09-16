from api import fetch_weather
from db import save_weather, get_last_entries

def main():
    city = input("Enter a city name: ")
    temp, desc = fetch_weather(city)
    if temp is not None:
        save_weather(city, temp, desc)
        print(f"{city}: {temp}°C, {desc}")
        
        print("\nLast entries for", city)
        for entry in get_last_entries(city):
            print(entry)

if __name__ == "__main__":
    main()
