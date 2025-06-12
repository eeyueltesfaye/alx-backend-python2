
"""
stream_users module

This module defines a generator function `stream_users`
that streams rows one by one from the user_data table
in the ALX_prodev MySQL database.
"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Load DB credentials from .env

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ALX_prodev"

def stream_users():
    """
    Generator that connects to the ALX_prodev database and yields rows
    from the user_data table one by one using a single loop.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        # Yield rows one by one (1 loop only)
        for row in cursor:
            yield row

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

