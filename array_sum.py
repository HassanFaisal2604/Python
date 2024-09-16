import numpy as np

def aVeryBigSum():
    # Taking input from the user as a space-separated string and converting it to a list of integers
    input1 = input("Enter the elements in the array separated by spaces: ")
    ar = np.array(list(map(int, input1.split())))  # Convert the input string to a NumPy array of integers
    
    total_sum = np.sum(ar)  # Sum the elements of the array
    print("The sum of the array elements is:", total_sum)

aVeryBigSum()
