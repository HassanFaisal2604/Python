def simpleArraySum(ar):
    # Initialize a variable to store the sum of the array elements
    total = 0
    
    # Iterate through each element in the array
    for num in ar:
        # Add each element to the total
        total += num
    
    # Return the total sum
    return total
if __name__ == '__main__':
    ar = [1, 2, 3, 4, 10, 11]
    result = simpleArraySum(ar)
    print(result)  # Output should be 31
