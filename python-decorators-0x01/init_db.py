import sqlite3

# Connect (or create) the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT INTO users (name, email) VALUES (?, ?)
''', [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
])

# Commit and close
conn.commit()
conn.close()

print("Database initialized with sample users.")
