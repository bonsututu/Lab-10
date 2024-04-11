import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('poems.db')
cursor = conn.cursor()

# Create a table to store poems
cursor.execute('''CREATE TABLE poems (
                    title TEXT,
                    author TEXT,
                    content TEXT
                )''')

# Commit changes and close connection
conn.commit()
conn.close()
