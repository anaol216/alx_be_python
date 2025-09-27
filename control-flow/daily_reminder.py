task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? ").lower()
if priority == "high" and time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
elif priority == "medium":
    print(f"Reminder: You have a medium-priority task '{task}'. Try to complete it soon.")
elif priority == "low":
    print(f"Reminder: You have a low-priority task '{task}'. You can attend to it at your convenience.")
else:
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
