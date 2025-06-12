import os
import mysql.connector  # For MySQL connection
import csv              # To read the CSV file
from mysql.connector import Error
import uuid 

from dotenv import load_dotenv


load_dotenv()

# Connects to the MySQL server (no specific DB yet)
def connect_db():
    try:
        return mysql.connector.connect(
            DB_HOST = os.getenv("DB_HOST"),
            DB_USER = os.getenv("DB_USER"),
            DB_PASSWORD = os.getenv("DB_PASSWORD")
      )
    except Error as err:
        print(f"Error connecting to MySQL Server: {err}")
        return None


# Creates the ALX_prodev database if it doesn't exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created (or already exists)")
        cursor.close()
    except Error as err:
        print(f"Error creating database: {err}")


# Connects directly to the ALX_prodev database
def connect_to_prodev():
    try:
        return mysql.connector.connect(
            DB_HOST = os.getenv("DB_HOST"),
            DB_USER = os.getenv("DB_USER"),
            DB_PASSWORD = os.getenv("DB_PASSWORD"),
            database="ALX_prodev"
        )
    except Error as err:
        print(f"Error connecting to ALX_prodev database: {err}")
        return None


# Creates the user_data table if it doesn't exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL
            )
        ''')
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except Error as err:
        print(f"Error creating table: {err}")


# Inserts user data from CSV file into the user_data table
def insert_data(connection, csv_file):
    try:
        with open(csv_file, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            cursor = connection.cursor()
            for row in reader:
                if len(row) < 3:
                    print(f"⚠️ Skipping invalid row: {row}")
                    continue
                user_id = str(uuid.uuid4())
                name, email, age = row
                cursor.execute('''
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                ''', (user_id, name, email, age))
            connection.commit()
            cursor.close()
            print(f"✅ Data from {csv_file} inserted successfully")
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
    except Error as err:
        print(f"❌ Error inserting data: {err}")

# Generator function that yields one row at a time from user_data table
def stream_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
