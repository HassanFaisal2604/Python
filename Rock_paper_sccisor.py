import random

u_count = 0  # User score
c_count = 0  # Computer score
choices = ['rock', 'paper', 'scissors']  # Possible choices

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
    print(f"Computer chose {computer_choice}.  chose {user_input}.")

    # Logic to determine the winner
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'scissors' and computer_choice == 'paper') or \
         (user_input == 'paper' and computer_choice == 'rock'):
        print("You win!")
        u_count += 1
    else:
        print("Computer wins!")
        c_count += 1

    # Show the score after each round
    print(f"Score: You - {u_count} | Computer - {c_count}")

# Print the final result
print(f"Final Score: You won {u_count} times. Computer won {c_count} times.")
