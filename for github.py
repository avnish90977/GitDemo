import time

# Get the current time
current_time = time.time()

print("Current Unix timestamp:", current_time)

# Convert the Unix timestamp to a readable format
formatted_time = time.ctime(current_time)
print("Current time:", formatted_time)

# Sleep for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake!")

# Measure the time taken by a piece of code
start_time = time.time()

# Your code here

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")
