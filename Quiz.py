count = 0

# First question
ques1 = "What is the capital of France?"
print(ques1)
print("A. London")
print("B. Paris")
print("C. Berlin")
print("D. Madrid")

ques = input("Your answer: ")

# First question using if-else
if ques.lower() == 'b' or ques.lower() == 'paris':
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

# Second question
ques2 = "What is the capital of Germany?"
print(ques2)
print("A. London")
print("B. Paris")
print("C. Berlin")
print("D. Madrid")

ques = input("Your answer: ")

# Second question using if-else
if ques.lower() == 'c' or ques.lower() == 'berlin':
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

# Final score
print(f"Your score is: {count}")
