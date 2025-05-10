import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")
        
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")

        choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()

        # Validate input
        while choice not in ("higher", "lower"):
            choice = input("Invalid input. Please enter either 'higher' or 'lower': ").lower()

        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_num}.")
            your_score += 1 
        else: 
            print(f"Aww, that's incorrect. The computer's number was {computer_num}.")

        print(f"Your score is now {your_score}")
        print()

    print(f"Your final score is {your_score} out of {NUM_ROUNDS}.")

    if your_score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("👍 Good job, you played really well!")
    else:
        print("🙁 Better luck next time!")

if __name__ == "__main__":
    main()
