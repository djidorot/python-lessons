import time

# Callback function definition
def callback_function(result):
    print(f"Callback function called. Result: {result}")

# Function simulating an asynchronous task
def perform_async_task(callback):
    print("Starting the asynchronous task.")
    
    # Simulate some time-consuming work
    time.sleep(3)
    
    result = 42  # Simulated result of the task
    
    # Call the callback function with the result
    callback(result)

# Main function to initiate the asynchronous task
def main():
    print("Main function starting.")

    # Pass the callback function to perform_async_task
    perform_async_task(callback_function)

    print("Main function continues without waiting for the task to finish.")

# Run the main function
if __name__ == "__main__":
    main()

