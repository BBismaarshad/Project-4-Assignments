import random

# Global constant for the number of sides on a die
NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints their total."""
    die1: int = random.randint(1, NUM_SIDES)  # Roll first die (1-6)
    die2: int = random.randint(1, NUM_SIDES)  # Roll second die (1-6)
    total: int = die1 + die2  # Calculate the total
    print("Total of two dice:", total)  # Print the total

def main():
    die1: int = 10  # Local variable in main()
    print("die1 in main() starts as: " + str(die1))  # Print initial value (10)
    
    # Roll dice three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    # Show that die1 in main() is unchanged (scope demonstration)
    print("die1 in main() is: " + str(die1))  # Still 10 (not affected by roll_dice())

if __name__ == '__main__':
    main()