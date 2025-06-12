"""
Simulates paginated lazy loading from MySQL using generators.
"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "ALX_prodev"


def paginate_users(page_size, offset):
    """
    Fetches a single page of users starting at the given offset.
    :param page_size: Number of records per page
    :param offset: Starting offset
    :return: List of user rows
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset)
        )
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows
    except mysql.connector.Error as err:
        print(f" Error: {err}")
        return []


def lazy_paginate(page_size):
    """
    Generator that lazily loads paginated user data one page at a time.
    :param page_size: Number of users per page
    """
    offset = 0

    #  Only one loop used
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
