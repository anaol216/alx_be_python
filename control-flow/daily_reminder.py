task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? ").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: You have a high-priority task '{task}' that is time-bound. Please address it immediately!")
        else:
            print(f"Reminder: You have a high-priority task '{task}'. Please address it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: You have a medium-priority task '{task}' that is time-bound. Please plan to complete it soon.")
        else:
            print(f"Reminder: You have a medium-priority task '{task}'. Please get to it when you can.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: You have a low-priority task '{task}' that is time-bound. Try to complete it when you have time.")
        else:
            print(f"Reminder: You have a low-priority task '{task}'. No rush, but don't forget about it!")
    case _:
        print("Error: Invalid priority level. Please enter high, medium, or low.")
        