task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unspecified priority."

if time_bound == "yes":
    reminder += " That requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

print("\nReminder:", reminder)

print("\nDon't forget your task! Here’s a quick reminder loop:")
for i in range(2):
    print(f"{i+1}. {reminder}")