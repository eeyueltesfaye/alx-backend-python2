
stream = __import__('0-stream_users').stream_users

print(" Streaming users one by one:")
for user in stream():
    print(user)
