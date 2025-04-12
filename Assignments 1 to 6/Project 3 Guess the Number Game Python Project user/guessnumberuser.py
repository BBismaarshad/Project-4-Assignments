import random  # Import random module to generate random numbers

def player_guesses():
    print("\n--- You Guess the Number ---")
    secret_number = random.randint(1, 10)  # Computer picks a random number
    attempts = 0  # Count how many tries player takes
    
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1  # Increase try count
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries!")
            break  # Exit loop when correct

def computer_guesses():
    print("\n--- Computer Guesses Your Number ---")
    print("Think of a number between 1 and 10.")
    input("Press Enter when you're ready...")  # Wait for player
    
    low = 1   # Minimum possible number
    high = 10 # Maximum possible number
    attempts = 0  # Count computer's tries
    
    while True:
        attempts += 1
        guess = random.randint(low, high)  # Computer makes random guess
        response = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if response == 'h':
            high = guess - 1  # Adjust maximum if too high
        elif response == 'l':
            low = guess + 1   # Adjust minimum if too low
        elif response == 'c':
            print(f"The computer guessed your number in {attempts} tries!")
            break  # Exit when correct
        else:
            print("Please enter H, L, or C.")  # Error message

print("Welcome to the Number Guessing Game!")
player_guesses()    # First game: you guess
computer_guesses()   # Second game: computer guesses