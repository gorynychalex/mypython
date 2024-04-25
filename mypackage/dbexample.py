import sqlite3

conn = sqlite3.connect("example.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))