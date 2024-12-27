task = input("Enter your task: ").title().strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

reminder = f"'{task}' is a {priority} priority task,"

# match time:
#     case "yes":
#         if priority == "high":
#             print(reminder + " task that requires immediate attention today!")
#         elif priority == "medium":
#             print(reminder + " ,Start after high priority Non-Time-Bound tasks")
#         elif priority == "low":
#             print(reminder + " As it has a deadline it should be done before mediume Non-Time-Bound tasks")
        
#     case "no":
#         if priority == "high":
#             print(reminder + " should start it once you completely finish high priority tasks")
#         elif priority == "medium":
#             print(reminder + " , start after low priority tasks")
#         elif priority == "low":
#             print(reminder + " Consider completing it when you have free time.")



match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task, Task that requires immediate attention today!")
        else:
            print(f"'{task}' is a {priority} priority task, Should start it once you completely finish high priority time bounded tasks")
    
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task, Start after high priority Non-Time-Bound tasks")
        else:
            print(f"'{task}' is a {priority} priority task, Start after low priority tasks")
    
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task, As it has a deadline it should be done before mediume Non-Time-Bound tasks")
        else:
            print(f"'{task}' is a {priority} priority task, Consider completing it when you have free time.")
