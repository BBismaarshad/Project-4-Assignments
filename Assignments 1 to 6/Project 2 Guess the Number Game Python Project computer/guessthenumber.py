import random 

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0  # Renamed to avoid confusion with function name
    
    while user_guess != random_number:
        try:
            user_guess = int(input(f"Guess a number between 1 and {x}: "))  # Convert input to int and use f-string
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if user_guess < random_number:
            print("Sorry, guess again. Too low.")
        elif user_guess > random_number:
            print("Sorry, guess again. Too high.")
        else:
            print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")

guess(10)