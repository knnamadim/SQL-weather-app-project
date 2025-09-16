# utils.py

def format_weather(city, temp, description):
    return f"Weather in {city}: {temp}°C, {description}"

def display_entries(entries):
    for e in entries:
        city, temp, desc, timestamp = e
        print(f"[{timestamp}] {city}: {temp}°C, {desc}")
