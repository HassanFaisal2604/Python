import random

u_count = 0  # User score
c_count = 0  # Computer score
choices = ['rock', 'paper', 'scissors']  # Possible choices
win_conditions = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

while True:
    # Get user's input
    user_input = input("Enter your input ['Rock', 'Paper', 'Scissors'] or 'exit' to stop: ").lower()
    
    # Allow user to exit the game
    if user_input == 'exit':
        print("Thanks for playing!")
        break

    # Check if the user's input is valid
    if user_input not in choices:
        print(f"Invalid input: {user_input}. Please choose from 'Rock', 'Paper', or 'Scissors'.")
        continue  # Ask for input again if invalid

    # Randomly select computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}. You chose {user_input}.")

    # Logic to determine the winner
    if user_input == computer_choice:
        print("It's a tie!")
    elif win_conditions[user_input] == computer_choice:
        print("You win!")
        u_count += 1
    else:
        print("Computer wins!")
        c_count += 1

    # Show the score after each round
    print(f"Score: You - {u_count} | Computer - {c_count}")

# Print the final result
print(f"Final Score: You won {u_count} times. Computer won {c_count} times.")