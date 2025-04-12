import random  # Import the random module to let the computer choose randomly

# Function to check if a player wins against the opponent
def is_win(player, opponent):
    # Winning conditions:
    # Rock ('r') beats Scissors ('s')
    # Scissors ('s') beats Paper ('p')
    # Paper ('p') beats Rock ('r')
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

# Main game function
def play():
    # Ask the user to choose Rock (r), Paper (p), or Scissors (s)
    user = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()  # Convert input to lowercase
    
    # Computer randomly selects Rock, Paper, or Scissors
    computer = random.choice(['r', 'p', 's'])
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    # Check if it's a tie (both chose the same)
    if user == computer:
        return "It's a tie!"
    
    # Check if the user wins
    if is_win(user, computer):
        return "You Won!! 🎉"
    
    # If not a tie and user didn't win, then user lost
    return "You lost! 😢"

# Start the game
print("--- Rock Paper Scissors Game ---")
print(play())