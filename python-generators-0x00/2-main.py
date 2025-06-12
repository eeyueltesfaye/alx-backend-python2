batch_processing = __import__('1-batch_processing').batch_processing

print("📤 Users over age 25 (batched):")
for user in batch_processing(3):
    print(user)