"""
Calculate average age using a generator for memory efficiency.
"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ALX_prodev"


def stream_user_ages():
    """
    Generator that yields user ages one by one from user_data table.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        # ✅ Loop 1: Yield ages one by one
        for (age,) in cursor:
            yield float(age)

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")


def calculate_average_age():
    """
    Uses stream_user_ages to compute and print average age.
    """
    total = 0
    count = 0

    # ✅ Loop 2: Consume ages and calculate average
    for age in stream_user_ages():
        total += age
        count += 1

    if count == 0:
        print("Average age of users: 0 (no users)")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")
