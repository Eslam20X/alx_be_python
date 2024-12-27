task = input("Enter your task: ").title().strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time = input("Is it time-bound? (yes/no): ").lower().strip()

reminder = f"'{task}' is a {priority} priority task,"

match time:
    case "yes":
        if priority == "high":
            print(reminder + " task that requires immediate attention today!")
        elif priority == "medium":
            print(reminder + " ,Start after high priority Non-Time-Bound tasks")
        elif priority == "low":
            print(reminder + " As it has a deadline it should be done before mediume Non-Time-Bound tasks")
        
    case "no":
        if priority == "high":
            print(reminder + " should start it once you completely finish high priority tasks")
        elif priority == "medium":
            print(reminder + " , start after low priority tasks")
        elif priority == "low":
            print(reminder + " Consider completing it when you have free time.")
