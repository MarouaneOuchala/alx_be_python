# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Generate reminder based on inputs
    match priority:
        case "high":
            message = f"'{task}' is a high-priority task."
        case "medium":
            message = f"'{task}' is a medium-priority task."
        case "low":
            message = f"'{task}' is a low-priority task."
        case _:
            print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
            return

    # Add urgency based on time sensitivity
    if time_bound == "yes":
        message += " It requires immediate attention today!"
    elif time_bound == "no":
        message += " Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return

    # Print the reminder
    print("\nReminder:", message)

if __name__ == "__main__":
    main()
