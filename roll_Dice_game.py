import random

def player_game():
    total_scores = {"Player 1": 0, "Player 2": 0}  # Track scores for both players
    turn_count = {"Player 1": 0, "Player 2": 0}
    
    players = ["Player 1", "Player 2"]  # List of players

    def play_turn(player):
        turn_score = 0  # Start a new turn for current player
        print(f"\n{player}'s turn! Total score: {total_scores[player]}")
        
        while True:  # Continue rolling within a single turn
            play = input(f'{player}, do you want to "roll", "hold", or "no" to exit: ')
            
            if play.lower() == 'no':
                print(f"Game over. {player}'s final score is {total_scores[player]} in {turn_count[player]} turns.")
                return True  # Indicates game should end
            
            if play.lower() == 'roll':
                di_num = random.randint(1, 6)  # Roll the dice
                print(f"{player} rolls: {di_num}")
                
                if di_num == 1:
                    print(f"{player} rolled a 1! You lose your points for this turn.")
                    turn_score = 0  # Reset turn score
                    break  # End turn and go back to outer loop to start a new turn
                else:
                    turn_score += di_num
                    print(f"{player}'s current turn score is {turn_score}.")
            
            elif play.lower() == 'hold':
                total_scores[player] += turn_score  # Add turn score to total score
                turn_count[player] += 1
                print(f"{player} holds! Total score is now {total_scores[player]}.")
                break  # End turn and go back to outer loop to start a new turn
            
            else:
                print('Invalid input. Please type "roll", "hold", or "no".')
        
        return False  # Indicates game should continue
    
    while True:
        for player in players:
            if play_turn(player):
                break  # Exit the game if "no" was entered

            # Check if any player has won after their turn
            if total_scores[player] >= 100:
                print(f"\nCongratulations! {player} won the game with a total score of {total_scores[player]} in {turn_count[player]} turns.")
                return

player_game()
