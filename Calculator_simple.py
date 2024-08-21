def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

# Ask the user for the calculation type and numbers
question = input("Which calculation do you want to perform (add, sub, multiply, divide)? ").strip().lower()
num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))

# Perform the calculation based on user input
if question == "add":
    print(f"Result: {add(num1, num2)}")
elif question == "sub":
    print(f"Result: {sub(num1, num2)}")
elif question == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif question == "divide":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation. Please choose add, sub, multiply, or divide.")
