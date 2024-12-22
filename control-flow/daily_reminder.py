# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Generate a reminder based on the priority and time sensitivity
match priority:
    case "high":
        Reminder = f"Your task: '{task}' is a HIGH priority task."
    case "medium":
        Reminder = f"Your task: '{task}' is a MEDIUM priority task."
    case "low":
        Reminder = f"Your task: '{task}' is a LOW priority task."
    case _:
        Reminder = f"Your task: '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    Reminder += " This task requires immediate attention today!"

# Print the final reminder
print("\n Reminder:")
print(Reminder)
print("----------------------")
