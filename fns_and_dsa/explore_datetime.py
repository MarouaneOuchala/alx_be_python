from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

# Function to calculate the future date
def calculate_future_date(): 
    # Get the current date
    current_date = datetime.now()
    
    # Prompt the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Add the days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date as a string
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Display the formatted future date
    print(f"The date after {days_to_add} days will be: {formatted_future_date}")
    
    return formatted_future_date

# Call the functions
display_current_datetime()
calculate_future_date()

