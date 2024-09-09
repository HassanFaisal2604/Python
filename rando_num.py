import random

def guess_game(my_list):
    guess_count = 0
    random_choice = random.choice(my_list).lower()

    while True:
        guess = input(f"Guess the item from this list {my_list}: ").lower()
        
        # Check if the guess is valid
        if guess not in my_list:
            print(f"{guess} is not in the list. Please try again.")
            continue
        
        guess_count += 1
        
        # Check if the guess is correct
        if guess == random_choice:
            print(f"Congrats! {guess} was the correct guess!")
            break
        else:
            print(f"Sorry, {guess} was not the correct guess. Try again.")
    
    print(f"You took {guess_count} attempt(s) to guess the correct item.")

# List of items
my_list = ['apple', 'banana', 'cherry', 'ali']
my_list1=[1,2,3,4,5,6,7]

# Start the game
guess_game(my_list)
