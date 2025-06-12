"""
Batch processing users from MySQL using generators
"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ALX_prodev"


def stream_users_in_batches(batch_size):
    """
    Generator that yields rows in batches from the user_data table.
    :param batch_size: Number of rows per batch
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

        # Loop 1: Fetch rows in batches using fetchmany()
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")


def batch_processing(batch_size):
    """
    Processes batches from stream_users_in_batches and yields users over age 25.
    :param batch_size: Size of the batch to fetch
    """
    # Loop 2: Iterate over batches
    for batch in stream_users_in_batches(batch_size):
        # Loop 3: Iterate over users in each batch
        for user in batch:
            age = float(user[3])  # Assuming age is in column index 3
            if age > 25:
                yield user
