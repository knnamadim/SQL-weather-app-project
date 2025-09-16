import sqlite3
import datetime

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    description TEXT,
    timestamp TEXT
)
""")
conn.commit()

def save_weather(city, temperature, description):
    timestamp = datetime.datetime.now().isoformat()
    cursor.execute("INSERT INTO weather (city, temperature, description, timestamp) VALUES (?, ?, ?, ?)",
                   (city, temperature, description, timestamp))
    conn.commit()

def get_last_entries(city, limit=5):
    cursor.execute("SELECT city, temperature, description, timestamp FROM weather WHERE city = ? ORDER BY id DESC LIMIT ?",
                   (city, limit))
    return cursor.fetchall()
