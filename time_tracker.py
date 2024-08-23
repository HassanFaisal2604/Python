task = ["Planning", "Design", "Coding", "Testing"]
time_spent = []

def log_time(task, time_spent):
    while True:
        take = int(input("Enter the task number (0 for Planning, 1 for Design, 2 for Coding, 3 for Testing, 4 to exit): "))
        
        if take == 4:
            break
        
        if take < len(task):
            if take == 0:
                input_time = int(input("Enter the amount of time you spent Planning: "))
            elif take == 1:
                input_time = int(input("Enter the amount of time you spent Designing: "))
            elif take == 2:
                input_time = int(input("Enter the amount of time you spent Coding: "))
            elif take == 3:
                input_time = int(input("Enter the amount of time you spent Testing: "))
            
            time_spent.append(input_time)
        else:
            print("Invalid task number. Please enter a number between 0 and 4.")
    
    print("\nTotal time spent on each task:")
    for i, time in enumerate(time_spent):
        print(f"{task[i]}: {time} hours")
    
log_time(task, time_spent)
