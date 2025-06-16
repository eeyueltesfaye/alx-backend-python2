import time
import sqlite3
import functools

query_cache = {}  # Global in-memory cache (key: query string, value: results)

# DB connection decorator (from earlier tasks)
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

#  Caching decorator
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("[CACHE] Returning cached result for query")
            return query_cache[query]

        print("[DB] Executing and caching result")
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call — hits the database
users = fetch_users_with_cache(query="SELECT * FROM users")
print("First call:", users)

# Second call — uses cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print("Second call:", users_again)
