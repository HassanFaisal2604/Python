Students = {}

def add_student(name, subject, marks):
    if name in Students:
        if subject in Students[name]:
            print(f"{name} already has a mark for {subject}.")
        else:
            Students[name][subject] = marks
            print(f"Added {subject} with marks {marks} for {name}.")
    else:
        Students[name] = {subject: marks}
        print(f"{name} added to the list with {subject} and marks {marks}.")

def display_students():
    for name, subjects in Students.items():
        print(f"{name}:")
        for subject, marks in subjects.items():
            print(f"  {subject}: {marks}")

# Testing the function
add_student("Ali", "Maths", 100)
add_student("Bob", "English", 90)

# Displaying the students dictionary
display_students()
