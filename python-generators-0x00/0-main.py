import seed

# Step 1: Connect to MySQL server (without DB)
connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("Initial connection and database creation successful")

    # Step 2: Connect to ALX_prodev DB
    connection = seed.connect_to_prodev()
    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')

        # Step 3: Print confirmation
        cursor = connection.cursor()
        cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print("✅ Database ALX_prodev is present")

        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print("✅ First 5 rows in user_data:")
        print(rows)
        cursor.close()

        # Step 4: Use generator
        print("\n Streaming rows using generator:")
        for row in seed.stream_users(connection):
            print(row)
        connection.close()
