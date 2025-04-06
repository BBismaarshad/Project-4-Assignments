import random

def main():
    target_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...", end=" ")
    
    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < target_number:
            print("Your guess is too low")
            print("Enter a new number:", end=" ")
        elif guess > target_number:
            print("Your guess is too high")
            print("Enter a new number:", end=" ")
        else:
            print(f"Congrats! The number was: {target_number}")
            break

if __name__ == '__main__':
    main()