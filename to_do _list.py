class to_do:
    from datetime import datetime

class Task:
    def __init__(self, title, description='', due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_completed = False
    
    def mark_completed(self):
        self.is_completed = True
    
    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else "No due date"
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {due_date_str}\nStatus: {status}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added to the list.")
    
    def remove_task(self, title):
        task = self.get_task(title)
        if task:
            self.tasks.remove(task)
            print(f"Task '{title}' removed from the list.")
        else:
            print(f"Task '{title}' not found.")
    
    def get_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None
    
    def mark_task_completed(self, title):
        task = self.get_task(title)
        if task:
            task.mark_completed()
            print(f"Task '{title}' marked as completed.")
        else:
            print(f"Task '{title}' not found.")
    
    def show_tasks(self, show_completed=True):
        if not self.tasks:
            print("No tasks in the list.")
            return
        
        for task in self.tasks:
            if show_completed or not task.is_completed:
                print(task)

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Show Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            due_date_input = input("Enter due date (YYYY-MM-DD, optional): ").strip()
            due_date = datetime.strptime(due_date_input, '%Y-%m-%d') if due_date_input else None
            
            task = Task(title, description, due_date)
            todo_list.add_task(task)
        
        elif choice == "2":
            title = input("Enter task title to remove: ").strip()
            todo_list.remove_task(title)
        
        elif choice == "3":
            title = input("Enter task title to mark as completed: ").strip()
            todo_list.mark_task_completed(title)
        
        elif choice == "4":
            show_completed = input("Show completed tasks? (y/n): ").strip().lower() == 'y'
            todo_list.show_tasks(show_completed=show_completed)
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")
