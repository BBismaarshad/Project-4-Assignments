import random

def main():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Calculate the total
    total = die1 + die2
    
    # Print the results
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()