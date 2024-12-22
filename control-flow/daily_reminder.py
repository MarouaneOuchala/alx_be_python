# daily_reminder.py

# Prompt the user for task details
Task = input("Enter your task description: ").strip()
Priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
Time_Bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Generate a reminder based on the priority and time sensitivity
match priority:
    case "high":
        reminder = f"Your task: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Your task: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Your task: '{task}' is a LOW priority task."
    case _:
        reminder = f"Your task: '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print("\n--- Daily Reminder ---")
print(reminder)
print("----------------------")

