# daily_reminder.py

while True:  # Loop so user can enter tasks again if they want
    # Step 1: Get task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Match Case for priority handling
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority level"

    # Step 3: Add time-sensitivity with if/else
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Step 4: Show the customized reminder
    print(f"Reminder: {reminder}")


    # Step 5: Ask if user wants to add another task
    again = input("\nWould you like to enter another task? (yes/no): ").lower()
    if again != "yes":
        print("Good luck with your tasks today!")
        break
