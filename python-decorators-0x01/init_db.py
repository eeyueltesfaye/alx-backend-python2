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


# Step 1: Modify the Table to Include age

import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Add 'age' column to users table
cursor.execute('''
    ALTER TABLE users ADD COLUMN age INTEGER DEFAULT NULL
''')

conn.commit()
conn.close()

print("Age column added successfully.")



# Step 2: Update Existing Users with Age

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Update users with sample ages
cursor.executemany('''
    UPDATE users SET age = ? WHERE name = ?
''', [
    (42, 'Alice'),
    (30, 'Bob'),
    (18, 'Charlie')
])

conn.commit()
conn.close()

print("User ages updated.")
